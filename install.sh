#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${APP_DIR:-$HOME/cv2}"
PORT="${PORT:-8000}"

if [[ ! -d "$APP_DIR" ]]; then
  mkdir -p "$APP_DIR"
  cp -R . "$APP_DIR"
fi

cd "$APP_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required. Please install it and re-run this script."
  exit 1
fi

if ! command -v pip3 >/dev/null 2>&1; then
  echo "pip3 not found. Installing python3-pip..."
  if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y python3-pip python3-venv
  else
    echo "No supported package manager found. Install pip3 manually."
    exit 1
  fi
fi

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

export PORT="$PORT"
python app.py
