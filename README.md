# MODS99 Passport Photo Tool (VPS Web App)

This repo now runs your passport photo web tool as a VPS-friendly Flask app that is reachable via `http://<server-ip>:<port>`.

## One-line install (from GitHub)

```bash
curl -fsSL https://raw.githubusercontent.com/maddix123/cv2/main/install.sh | bash
```

Optional custom port:

```bash
PORT=9000 curl -fsSL https://raw.githubusercontent.com/maddix123/cv2/main/install.sh | bash
```

The installer will:
- Clone/update `maddix123/cv2`
- Create a Python virtualenv
- Install dependencies
- Start the app in the background with `nohup`
- Print the VPS URL (`ip:port`) to open in a browser

## Manual run

```bash
git clone https://github.com/maddix123/cv2.git
cd cv2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
HOST=0.0.0.0 PORT=8000 python app.py
```

Then open `http://<your-vps-ip>:8000`.
