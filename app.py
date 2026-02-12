from __future__ import annotations

import os
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "cv2.db"

app = Flask(__name__)
app.secret_key = os.environ.get("CV2_SECRET", "change-me")


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_error: BaseException | None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


@app.before_request
def ensure_db() -> None:
    init_db()


def current_user_id() -> int | None:
    user_id = session.get("user_id")
    return int(user_id) if user_id is not None else None


@app.route("/")
def index():
    if not current_user_id():
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user_id():
        return redirect(url_for("index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.", "error")
            return redirect(url_for("signup"))

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (email, password_hash, created_at) VALUES (?, ?, ?)",
                (email, generate_password_hash(password), datetime.utcnow().isoformat()),
            )
            db.commit()
        except sqlite3.IntegrityError:
            flash("That email is already registered.", "error")
            return redirect(url_for("signup"))

        flash("Account created. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user_id():
        return redirect(url_for("index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        db = get_db()
        user = db.execute(
            "SELECT id, password_hash FROM users WHERE email = ?",
            (email,),
        ).fetchone()

        if not user or not check_password_hash(user["password_hash"], password):
            flash("Invalid credentials.", "error")
            return redirect(url_for("login"))

        session["user_id"] = user["id"]
        flash("Logged in successfully.", "success")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", 8000)),
    )
