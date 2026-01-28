from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.models.risk_record import RiskRecord
from app.extensions import db

main = Blueprint("main", __name__)

@main.route("/dashboard")
@login_required
def dashboard():
    history = RiskRecord.query.filter_by(
        user_id=current_user.id
    ).order_by(RiskRecord.created_at.desc()).all()

    return render_template("dashboard.html", history=history)


@main.route("/calculate-risk", methods=["POST"])
@login_required
def calculate_risk():
    data = request.get_json()

    income = float(data.get("income", 0))
    debt = float(data.get("debt", 0))
    credit = int(data.get("credit", 0))

    if credit < 300 or credit > 900:
        return jsonify({"error": "Invalid credit score"}), 400

    # Simple risk logic
    if debt > income or credit < 600:
        risk = "High"
    elif credit < 700:
        risk = "Medium"
    else:
        risk = "Low"

    record = RiskRecord(
        user_id=current_user.id,
        income=income,
        debt=debt,
        credit_score=credit,
        risk_level=risk
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({"risk": risk})
