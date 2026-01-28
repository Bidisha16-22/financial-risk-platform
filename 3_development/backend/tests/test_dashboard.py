def test_dashboard_access(client):
    client.post("/register", data={
        "email": "dash@test.com",
        "password": "123456"
    })

    response = client.get("/dashboard")
    assert response.status_code == 200
