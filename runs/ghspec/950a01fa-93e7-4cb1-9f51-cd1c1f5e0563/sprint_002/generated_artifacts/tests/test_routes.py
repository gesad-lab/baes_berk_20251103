```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.db import init_db, shutdown_db  # Assuming database initialization functions
from src.models import User  # Assuming you have a User model

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    yield
    shutdown_db()

@pytest.fixture
def client():
    """Create a TestClient for testing API endpoints."""
    with TestClient(app) as client:
        yield client

def test_create_user_success(client):
    """Test creating a user successfully."""
    response = client.post(
        "/api/v1/users",
        json={"username": "testuser", "email": "testuser@example.com", "password": "Password123"},
    )
    assert response.status_code == 201  # Check for Created status
    assert response.json() == {"username": "testuser", "email": "testuser@example.com"}

def test_create_user_failure_missing_field(client):
    """Test creating a user fails when required fields are missing."""
    response = client.post(
        "/api/v1/users",
        json={"username": "testuser"},  # Missing email and password
    )
    assert response.status_code == 422  # Check for Unprocessable Entity status
    assert "email" in response.json()['detail'][0]['loc']  # Check that email is in the errors

def test_get_user_success(client):
    """Test retrieving a user successfully."""
    client.post(
        "/api/v1/users",
        json={"username": "testuser", "email": "testuser@example.com", "password": "Password123"},
    )
    response = client.get("/api/v1/users/testuser")
    assert response.status_code == 200  # Check for OK status
    assert response.json() == {"username": "testuser", "email": "testuser@example.com"}

def test_get_user_failure_not_found(client):
    """Test retrieving a user that does not exist."""
    response = client.get("/api/v1/users/nonexistentuser")
    assert response.status_code == 404  # Check for Not Found status
    assert response.json() == {"detail": "User not found"}

def test_create_multiple_users(client):
    """Test creating multiple users."""
    usernames = [f"user{i}" for i in range(2, 5)]
    for username in usernames:
        response = client.post(
            "/api/v1/users",
            json={"username": username, "email": f"{username}@example.com", "password": "Password123"},
        )
        assert response.status_code == 201  # Check for Created status
        assert response.json()["username"] == username
```