# tests/test_teachers.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_teacher_valid():
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher created successfully",
        "teacher": {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }

def test_create_teacher_missing_name():
    """Test creating a teacher without a name."""
    response = client.post("/teachers", json={"email": "invalid@example.com"})
    assert response.status_code == 422  # Unprocessable Entity for missing required fields
    assert response.json() == {"error": {"code": "E003", "message": "Missing required field: name"}}

def test_create_teacher_missing_email():
    """Test creating a teacher without an email."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 422  # Unprocessable Entity for missing required fields
    assert response.json() == {"error": {"code": "E003", "message": "Missing required field: email"}}

def test_create_teacher_invalid_email_format():
    """Test creating a teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity for invalid email format
    assert response.json() == {"error": {"code": "E004", "message": "Invalid email format"}}

def test_get_teachers():
    """Test retrieving all teachers."""
    response = client.get("/teachers")
    assert response.status_code == 200
    assert "teachers" in response.json()  # Ensure the response contains teachers
    assert isinstance(response.json()["teachers"], list)  # Check that teachers is a list
