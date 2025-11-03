from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student_valid():
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    # Assert that the creation was successful and response format is as expected
    assert response.status_code == 200
    assert response.json() == {"message": "Student created successfully", "student": {"name": "John Doe", "email": "john.doe@example.com"}}

def test_create_student_empty_name():
    """Test creating a student with an empty name."""
    response = client.post("/students", json={"name": "", "email": "john.doe@example.com"})
    # Assert that the response contains an appropriate error message for missing name
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_create_student_invalid_email():
    """Test creating a student with an invalid email address format."""
    # Test with an improperly formatted email
    response_invalid_format = client.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response_invalid_format.status_code == 422  # Unprocessable Entity for email validation
    assert response_invalid_format.json() == {"error": {"code": "E002", "message": "Invalid email format"}}  # Assuming this is the expected error format

    # Test with a blank email
    response_blank_email = client.post("/students", json={"name": "Jane Doe", "email": ""})
    assert response_blank_email.status_code == 400  # Bad Request for empty email
    assert response_blank_email.json() == {"error": {"code": "E003", "message": "Email is required"}}  # Assuming this is the expected error format

def test_get_students():
    """Test retrieving all students."""
    response = client.get("/students")
    assert response.status_code == 200
    assert "students" in response.json()