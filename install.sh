#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/maddix123/cv2.git"
APP_DIR="${APP_DIR:-$HOME/cv2}"
PORT="${PORT:-8000}"
HOST="${HOST:-0.0.0.0}"

if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update -y
  sudo apt-get install -y git python3 python3-venv python3-pip
fi

if [[ -d "$APP_DIR/.git" ]]; then
  git -C "$APP_DIR" pull --ff-only
else
  rm -rf "$APP_DIR"
  git clone "$REPO_URL" "$APP_DIR"
fi

cd "$APP_DIR"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

nohup env HOST="$HOST" PORT="$PORT" .venv/bin/python app.py > app.log 2>&1 &

IP_ADDR="$(hostname -I | awk '{print $1}')"
echo "CV2 Passport tool started."
echo "Open: http://${IP_ADDR}:${PORT}"
echo "Logs: tail -f $APP_DIR/app.log"
