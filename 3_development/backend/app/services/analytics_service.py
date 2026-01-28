from app.models.risk_record import RiskRecord

def get_summary():
    records = RiskRecord.query.all()
    return {
        "high": sum(1 for r in records if r.risk_level == "High"),
        "medium": sum(1 for r in records if r.risk_level == "Medium"),
        "low": sum(1 for r in records if r.risk_level == "Low")
    }
