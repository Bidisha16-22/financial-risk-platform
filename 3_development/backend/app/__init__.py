from flask import Flask
from app.extensions import db, login_manager

def create_app(testing=False):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///risk.db"

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import models
    from app.models.user import User
    from app.models.risk_record import RiskRecord

    # Register blueprints
    from app.routes.auth_routes import auth
    from app.routes.main_routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
