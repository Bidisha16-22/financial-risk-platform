def test_risk_calculation(client):
    client.post("/register", data={
        "email": "risk@test.com",
        "password": "123456"
    })

    response = client.post("/calculate-risk", json={
        "income": 100000,
        "debt": 150000,
        "credit": 650
    })

    assert response.json["risk"] in ["High", "Medium", "Low"]
