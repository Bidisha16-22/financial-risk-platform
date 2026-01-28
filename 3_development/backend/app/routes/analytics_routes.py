from flask import Blueprint, jsonify
from flask_login import login_required
from app.services.analytics_service import get_summary

analytics = Blueprint("analytics", __name__)

@analytics.route("/risk-summary")
@login_required
def summary():
    return jsonify(get_summary())
