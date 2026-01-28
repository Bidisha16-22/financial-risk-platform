def test_register(client):
    response = client.post("/register", data={
        "email": "testuser@example.com",
        "password": "test123"
    }, follow_redirects=True)

    assert b"Dashboard" in response.data


def test_login_invalid(client):
    response = client.post("/", data={
        "email": "wrong@example.com",
        "password": "wrong"
    })

    assert b"not registered" in response.data
