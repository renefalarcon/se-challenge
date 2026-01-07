from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={
        "username": "testuser",
        "email": "test@test.com",
        "first_name": "Test",
        "last_name": "User",
        "role": "user"
    })
    assert response.status_code == 200
