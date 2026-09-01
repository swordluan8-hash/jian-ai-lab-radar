#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: install.sh /absolute/path/to/Jian-AI-Lab-最高工作制度档案-版本17.md" >&2
  exit 2
fi

policy_path="$1"
if [[ ! -f "$policy_path" ]]; then
  echo "policy file not found: $policy_path" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skill_source="$(cd "$script_dir/.." && pwd)"
hermes_root="${HERMES_HOME:-${HOME}/.hermes}"
skill_target="$hermes_root/skills/jian-ai-lab-automation"

mkdir -p "$skill_target/scripts"
cp "$skill_source/SKILL.md" "$skill_target/SKILL.md"
cp "$skill_source/scripts/preflight.py" "$skill_target/scripts/preflight.py"
cp "$skill_source/scripts/authorize.py" "$skill_target/scripts/authorize.py"
chmod 0755 "$skill_target/scripts/preflight.py" "$skill_target/scripts/authorize.py"

config_dir="$hermes_root/jian-ai-lab"
mkdir -p "$config_dir"
printf '%s\n' "$policy_path" > "$config_dir/policy-path.txt"

echo "installed: $skill_target"
echo "policy: $policy_path"
echo "next: hermes skills list"
echo "scheduled automation remains disabled until Hermes passes acceptance and authorize.py is run"
