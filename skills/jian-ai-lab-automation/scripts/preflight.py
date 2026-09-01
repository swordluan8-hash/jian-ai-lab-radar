#!/usr/bin/env python3
"""Fail-closed preflight for a Jian AI Lab daily run."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_POLICY_MARKERS = (
    "剑的 AI 实验室最高工作制度",
    "这份档案是每天工作的唯一执行依据",
    "人工开始或已授权的 Hermes 定时开始",
    "用户不需要每天重复说“开始”",
    "文章和视频开头必须用陈述句直接说出痛点、帮助和结果",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_file(path: Path, label: str) -> str:
    if not path.is_file():
        raise ValueError(f"{label} does not exist: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"{label} is empty: {path}")
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", required=True, type=Path)
    parser.add_argument("--review", required=True, type=Path)
    start = parser.add_mutually_exclusive_group(required=True)
    start.add_argument("--start-signal")
    start.add_argument("--automation-authorization", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = {
        "status": "blocked",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "policy_path": str(args.policy.expanduser().resolve()),
        "review_path": str(args.review.expanduser().resolve()),
    }

    try:
        policy = args.policy.expanduser().resolve()
        review = args.review.expanduser().resolve()
        policy_text = require_file(policy, "policy")
        require_file(review, "previous Review")

        missing = [m for m in REQUIRED_POLICY_MARKERS if m not in policy_text]
        if missing:
            raise ValueError("policy is missing required markers: " + " | ".join(missing))

        policy_hash = sha256(policy)
        if args.start_signal is not None:
            signal = args.start_signal.strip()
            if signal not in {"开始今天的工作", "开始执行"}:
                raise ValueError("no valid explicit start signal")
            execution_mode = "manual"
            authorization_path = None
        else:
            authorization_path = args.automation_authorization.expanduser().resolve()
            authorization_text = require_file(authorization_path, "automation authorization")
            authorization = json.loads(authorization_text)
            required_scopes = {"daily_start", "website_update", "platform_publish"}
            scopes = set(authorization.get("scopes", []))
            if authorization.get("enabled") is not True:
                raise ValueError("scheduled automation is not enabled")
            if authorization.get("policy_sha256") != policy_hash:
                raise ValueError("scheduled authorization does not match current policy SHA-256")
            if not required_scopes.issubset(scopes):
                raise ValueError("scheduled authorization is missing required scopes")
            signal = "authorized Hermes schedule"
            execution_mode = "scheduled"

        manifest.update(
            {
                "status": "ready",
                "policy_sha256": policy_hash,
                "policy_size_bytes": policy.stat().st_size,
                "review_sha256": sha256(review),
                "start_signal": signal,
                "execution_mode": execution_mode,
                "automation_authorization_path": (
                    str(authorization_path) if authorization_path is not None else None
                ),
            }
        )
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError, TypeError) as exc:
        manifest["error"] = str(exc)

    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False))
    return 0 if manifest["status"] == "ready" else 2


if __name__ == "__main__":
    raise SystemExit(main())
