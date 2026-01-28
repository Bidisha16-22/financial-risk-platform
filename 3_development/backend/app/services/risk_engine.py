def calculate_risk(income, debt, credit):
    score = 0

    if income < 30000:
        score += 40
    elif income < 70000:
        score += 20

    if debt > income * 0.5:
        score += 40
    elif debt > income * 0.3:
        score += 20

    if credit < 600:
        score += 30
    elif credit < 700:
        score += 15

    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"
