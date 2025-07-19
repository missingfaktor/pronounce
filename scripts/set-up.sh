#!/usr/bin/env bash

set -euo pipefail

if ! command -v uv &> /dev/null; then
  echo "❌ 'uv' not found. Please install it:"
  echo "    curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 1
fi

uv venv --allow-existing

uv lock

uv sync
