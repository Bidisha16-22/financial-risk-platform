from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.services.risk_engine import calculate_risk
from app.models.risk_record import RiskRecord
from app import db

risk = Blueprint("risk", __name__)

@risk.route("/calculate-risk", methods=["POST"])
@login_required
def calculate():
    d = request.json
    level = calculate_risk(d["income"], d["debt"], d["credit"])

    record = RiskRecord(
        user_id=current_user.id,
        income=d["income"],
        debt=d["debt"],
        credit_score=d["credit"],
        risk_level=level
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({"risk_level": level})
