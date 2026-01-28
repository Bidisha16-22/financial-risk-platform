import os

class Config:
    # ---------------- SECURITY ----------------
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "final-finrisk-secret"   # fallback for local/dev
    )

    # ---------------- DATABASE ----------------
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///risk.db"      # local database
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---------------- MONITORING / MAINTENANCE ----------------
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
