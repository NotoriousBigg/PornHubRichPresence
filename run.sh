#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/src"

python3 -m pip install -r requirements.txt --quiet

python3 main.py
