```
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.teacher import Teacher
from src.services.teacher_service import create_teacher, get_teacher_by_email
from src.repositories.teacher_repository import create_teacher_repository
from src.database import get_db

client = TestClient(app)

# Sample test data for teachers
valid_teacher_data = {
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
}

invalid_teacher_data = {
    "name": "",
    "email": "invalid-email"
}

@pytest.fixture(scope="module")
def test_database():
    # Set up the test database connection
    db = get_db()
    yield db
    # Tear down the database connection
    db.close()

def test_create_teacher_success(test_database):
    response = client.post("/teachers/", json=valid_teacher_data)
    assert response.status_code == 201
    assert response.json()["name"] == valid_teacher_data["name"]
    assert response.json()["email"] == valid_teacher_data["email"]

def test_create_teacher_missing_name(test_database):
    response = client.post("/teachers/", json={"email": valid_teacher_data["email"]})
    assert response.status_code == 422  # Unprocessable Entity

def test_create_teacher_invalid_email(test_database):
    response = client.post("/teachers/", json=invalid_teacher_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_create_teacher_duplicate_email(test_database):
    # First teacher creation should succeed
    client.post("/teachers/", json=valid_teacher_data)
    # Second creation with the same email should fail
    response = client.post("/teachers/", json=valid_teacher_data)
    assert response.status_code == 400  # Bad Request
    assert response.json()["detail"] == "Email already exists"
    
def test_get_teacher_by_email_success(test_database):
    client.post("/teachers/", json=valid_teacher_data)
    response = client.get(f"/teachers/{valid_teacher_data['email']}")
    assert response.status_code == 200
    assert response.json()["email"] == valid_teacher_data["email"]

def test_get_teacher_by_nonexistent_email(test_database):
    response = client.get("/teachers/nonexistent@example.com")
    assert response.status_code == 404  # Not Found
```