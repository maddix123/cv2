#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${APP_DIR:-$HOME/cv2}"
PORT="${PORT:-8000}"

if [[ ! -d "$APP_DIR" ]]; then
  mkdir -p "$APP_DIR"
  cp -R . "$APP_DIR"
fi

cd "$APP_DIR"

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install flask werkzeug

export PORT="$PORT"
python app.py
