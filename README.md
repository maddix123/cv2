# CV2 VPS Resume Builder

CV2 is a lightweight VPS-hosted CV builder that requires users to sign up and log in before generating exports. It offers 50 templates and produces PDF, Word, and PNG downloads.

## Install (one-line format requested)

```bash
curl -fsSL https://raw.githubusercontent.com/maddix123/cv2/main/install.sh -o install.sh
chmod +x install.sh
./install.sh
```

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then visit `http://<ip>:8000` on your VPS.

## Notes

- Exports are generated on the server inside the `exports/` directory.
- For production use, set `CV2_SECRET` and run behind a reverse proxy.
