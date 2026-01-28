from app.extensions import db
from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

class RiskRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    income = db.Column(db.Float)
    debt = db.Column(db.Float)
    credit_score = db.Column(db.Integer)
    risk_level = db.Column(db.String(20))
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(IST)
    )

