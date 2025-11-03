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
    """Create a TestClient for testing the FastAPI app."""
    with TestClient(app) as client:
        yield client

def test_create_user(client):
    """Test client can create a user successfully."""
    response = client.post(
        "/api/v1/users",
        json={"username": "testuser", "email": "testuser@example.com", "password": "securepassword"}
    )
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_create_user_duplicate(client):
    """Test creating a user with a duplicate username fails."""
    client.post("/api/v1/users", json={"username": "testuser", "email": "testuser@example.com", "password": "securepassword"})
    response = client.post(
        "/api/v1/users",
        json={"username": "testuser", "email": "other@example.com", "password": "securepassword"}
    )
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"  # Assuming this error code for duplicates

def test_get_user(client):
    """Test retrieving a user by username."""
    response = client.get("/api/v1/users/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_get_user_not_found(client):
    """Test retrieving a non-existing user returns 404."""
    response = client.get("/api/v1/users/nonexistentuser")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E002"  # Assuming this error for not found

def test_get_all_users(client):
    """Test retrieving all users returns appropriate structure."""
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```
