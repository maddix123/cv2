# MODS99 Passport Photo Tool (VPS Web App)

This repo runs your passport photo tool as a VPS-friendly Flask app reachable via `http://<server-ip>:<port>`.

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
- Create the app database/tables automatically (for user login + saved work)
- Start the app in the background with `nohup`
- Print the VPS URL (`ip:port`) to open in a browser

## How auth works

- `/` shows Home with visible **Login** and **Sign Up** buttons.
- `/login` and `/signup` handle account access.
- `/app` is the passport tool (requires login).
- Inside the tool, click **Save Online** to store your current work in the database.

## Manual run

```bash
git clone https://github.com/maddix123/cv2.git
cd cv2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -c "from app import init_db; init_db()"
HOST=0.0.0.0 PORT=8000 python app.py
```

Then open `http://<your-vps-ip>:8000`.
