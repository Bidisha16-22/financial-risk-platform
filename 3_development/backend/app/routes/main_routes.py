import logging
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.models.risk_record import RiskRecord
from app.extensions import db

main = Blueprint("main", __name__)

# ---------------- DASHBOARD ----------------
@main.route("/dashboard")
@login_required
def dashboard():
    history = RiskRecord.query.filter_by(
        user_id=current_user.id
    ).order_by(RiskRecord.created_at.desc()).all()

    logging.info(f"Dashboard accessed by user_id={current_user.id}")

    return render_template("dashboard.html", history=history)


# ---------------- RISK CALCULATION ----------------
@main.route("/calculate-risk", methods=["POST"])
@login_required
def calculate_risk():
    data = request.get_json()

    income = float(data.get("income", 0))
    debt = float(data.get("debt", 0))
    credit = int(data.get("credit", 0))

    logging.info(
        f"Risk calculation requested by user_id={current_user.id} | "
        f"income={income}, debt={debt}, credit={credit}"
    )

    if credit < 300 or credit > 900:
        logging.warning(
            f"Invalid credit score submitted by user_id={current_user.id}"
        )
        return jsonify({"error": "Invalid credit score"}), 400

    # -------- Risk Logic --------
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

    logging.info(
        f"Risk calculated for user_id={current_user.id} | result={risk}"
    )

    return jsonify({"risk": risk})


# ---------------- HEALTH CHECK (MONITORING / UPTIME) ----------------
@main.route("/health")
def health():
    logging.info("Health check endpoint accessed")
    return jsonify({"status": "UP"}), 200
