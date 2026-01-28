# API Design

## Authentication APIs

### POST /register
Request:
{
  "email": "user@example.com",
  "password": "password"
}

Response:
{
  "message": "User registered successfully"
}

---

### POST /login
Request:
{
  "email": "user@example.com",
  "password": "password"
}

Response:
{
  "message": "Login successful"
}

---

## Risk Assessment APIs

### POST /calculate-risk
Request:
{
  "income": 50000,
  "debt": 12000,
  "credit_score": 680
}

Response:
{
  "risk_level": "Medium",
  "risk_score": 55
}

---

## Analytics APIs

### GET /risk-summary
Response:
{
  "high": 10,
  "medium": 25,
  "low": 15
}
