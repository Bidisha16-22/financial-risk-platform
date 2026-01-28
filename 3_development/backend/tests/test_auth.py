def test_register(client):
    response = client.post("/register", data={
        "email": "test@test.com",
        "password": "123456"
    }, follow_redirects=True)

    assert b"Dashboard" in response.data
