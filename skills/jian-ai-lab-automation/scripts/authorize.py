#!/usr/bin/env python3
"""Bind scheduled Jian AI Lab permissions to one exact policy revision."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    policy = args.policy.expanduser().resolve()
    text = policy.read_text(encoding="utf-8")
    required = (
        "Hermes 自动执行版",
        "用户不需要每天重复说“开始”",
        "按固定平台顺序自动发布",
    )
    missing = [marker for marker in required if marker not in text]
    if missing:
        raise SystemExit("policy does not authorize scheduled publishing: " + " | ".join(missing))

    authorization = {
        "enabled": True,
        "approved_at": datetime.now(timezone.utc).isoformat(),
        "policy_path": str(policy),
        "policy_sha256": sha256(policy),
        "scopes": ["daily_start", "website_update", "platform_publish"],
    }
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(authorization, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(authorization, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
