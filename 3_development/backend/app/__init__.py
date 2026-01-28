import logging
from flask import Flask
from app.extensions import db, login_manager

def create_app(testing=False):
    app = Flask(__name__)

    # ---------------- BASIC CONFIG ----------------
    app.config["SECRET_KEY"] = "dev-secret"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ---------------- DATABASE CONFIG ----------------
    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///risk.db"

    # ---------------- MONITORING (LOGGING) ----------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    app.logger.info("🚀 Financial Risk Platform starting")

    # ---------------- INITIALIZE EXTENSIONS ----------------
    db.init_app(app)
    login_manager.init_app(app)

    # ---------------- IMPORT MODELS ----------------
    from app.models.user import User
    from app.models.risk_record import RiskRecord

    # ---------------- REGISTER BLUEPRINTS ----------------
    from app.routes.auth_routes import auth
    from app.routes.main_routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    # ---------------- CREATE TABLES ----------------
    with app.app_context():
        db.create_all()
        app.logger.info("✅ Database initialized")

    return app
