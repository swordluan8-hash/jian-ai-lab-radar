---
name: jian-ai-lab-automation
description: Run Jian AI Lab preparation and publishing workflows under the current highest-policy file, with explicit start and approval gates.
metadata:
  hermes:
    version: 0.1.0
    platforms: [macos, linux]
    tags: [jian-ai-lab, publishing, automation, policy]
    category: operations
    requires_toolsets: [terminal]
---

# Jian AI Lab Automation

## When to Use

Use this skill for `剑的 AI 实验室 / Jian AI Lab` preparation, daily workflow orchestration, Hermes scheduling design, and controlled platform publishing.

Canonical site identity:

- Production: `https://jianailab.com`
- ChatGPT Sites slug: `jian-ai-lab`
- Radar repository: `swordluan8-hash/jian-ai-lab-radar`

Do not create a replacement site or infer a Sites project ID.

## Authoritative Policy

The current local file named `Jian-AI-Lab-最高工作制度档案-版本17.md` is the only operational authority. Its internal revision label may differ from the stable filename; do not rename, summarize, merge, or silently rewrite it.

Before any daily work:

1. Resolve the policy path from `JIAN_AI_LAB_POLICY_PATH` or an explicit user-provided path.
2. Run `scripts/preflight.py` with the policy, previous Review, and either an explicit start signal or the active scheduled-authorization file.
3. Read the complete policy and previous Review after preflight passes.
4. Follow their current order, ownership, review gates, and publishing rules exactly.
5. If another instruction conflicts, stop and report the exact conflict. The policy wins unless the user explicitly updates it.

Never embed an old snapshot of the policy into this skill and call it current. Record its SHA-256 in every run manifest so the user can identify exactly which revision was executed.

## Modes

### Deployment mode

Deployment mode may install or validate Hermes, install this skill, configure read-only connections, and run health checks. It must not run the daily radar, write articles, modify the website, contact authors, publish posts, or create a publishing cron job.

### Daily execution mode

Before Hermes acceptance, daily execution requires a fresh explicit start signal from the user. After Hermes acceptance and scheduled authorization, the scheduled fire is the daily start signal. Passing preflight opens the first policy-defined stage. Complete every stage and its self-check before advancing.

### Scheduled mode

Scheduled execution is allowed only after all of these are true:

1. Hermes passes installation and connection checks on the target host.
2. This skill is installed and visible to Hermes.
3. `scripts/authorize.py` creates an authorization file for the exact current policy SHA-256.
4. A scheduled preflight succeeds and a stale-policy-hash test fails closed.
5. The cron job has this skill attached and preserves a manual pause/kill switch.

The scheduled job may then run the policy-defined daily workflow, update the website, and publish completed, self-checked content on the fixed platforms without asking the user to say “开始” or approve each platform every day.

## Writing Control

Use the verified experiment report as the single factual source. Before delivering any article, verify that it:

- follows the writing structure in the exact policy revision recorded by preflight;
- opens with a declarative statement of the pain, help, and result;
- leads with user benefit, project strength, replacement value, and measured result;
- states only failures that actually occurred;
- does not invent fees, risks, results, rankings, repository facts, or author identities;
- remains a draft until the required user approval is recorded.

An older draft is not evidence that the current policy was followed. If its policy hash is absent or differs, re-check it against the current policy before publication.

## External Actions

Treat website deployment, GitHub publication, author contact, and platform posting as external actions. When scheduled authorization is valid, the current policy supplies standing permission for its fixed daily workflow, website updates, and fixed-platform publishing. Prepare and self-check exact content and evidence before each action. Stop on login loss, verification challenge, payment, subscription purchase, account risk, fact conflict, missing required material, or a failed publish; report the blocker instead of bypassing or repeatedly retrying it. A file upload, preview, or draft is not a successful publication.

Never expose OAuth tokens, cookies, API keys, verification codes, or private contact records in reports, prompts, repositories, or logs.

## Verification

For deployment:

1. `hermes --version` succeeds on the target Mac or Linux host.
2. `hermes doctor` completes without an unresolved blocking error.
3. `hermes skills list` contains `jian-ai-lab-automation`.
4. `scripts/preflight.py` produces `status: ready` for both a valid manual start and a valid scheduled authorization.
5. A missing authorization and a stale policy SHA-256 must fail closed and make no external change.
6. The first scheduled run is observed end-to-end before unattended daily execution is considered accepted.

Report target host, Hermes version, installed skill path, policy path, policy SHA-256, Review path, test results, and any unresolved blocker. Never report deployment complete merely because files were prepared elsewhere.
