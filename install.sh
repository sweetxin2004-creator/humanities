#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
export UV_CACHE_DIR="$ROOT/.local/uv-cache"
export npm_config_cache="$ROOT/.local/npm-cache"
python3 scripts/install_skills.py
uv sync --frozen --no-dev --project "$ROOT/.local/skill-sources/paper-search-mcp"
if [[ ! -x "$ROOT/.local/humanities-venv/bin/python" ]]; then
  uv venv "$ROOT/.local/humanities-venv"
fi
uv pip sync --python "$ROOT/.local/humanities-venv/bin/python" --require-hashes requirements.humanities.lock
npm ci --prefix tools/chrome-devtools --no-audit --no-fund
bash startup.sh
