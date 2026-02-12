# MODS99 Passport Photo Tool (VPS App)

A VPS-ready web app with:
- Passport photo editor (upload, crop, preview, PDF export)
- Login & signup
- Online save/load of your work per user account

## One-line install

```bash
curl -fsSL https://raw.githubusercontent.com/maddix123/cv2/main/install.sh | bash
```

Optional custom port:

```bash
PORT=9000 curl -fsSL https://raw.githubusercontent.com/maddix123/cv2/main/install.sh | bash
```

## Routes

- `/` → Home page with visible **Login** and **Sign Up** buttons
- `/login` → Login form
- `/signup` → Signup form
- `/app` → Passport editor (login required)
- `/save-work` → Save current work online (login required)
- `/load-work` → Load latest saved work (login required)

## Database behavior

- Installer creates DB tables during deployment.
- App also calls `init_db()` before requests, so tables are auto-created if missing.
- User credentials and saved work are stored in SQLite file `cv2.db`.

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
