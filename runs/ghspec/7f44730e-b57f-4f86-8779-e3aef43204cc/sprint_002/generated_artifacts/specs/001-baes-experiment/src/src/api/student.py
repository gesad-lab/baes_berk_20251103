from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student_valid():
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    # Assert that the creation was successful and response format is as expected
    assert response.status_code == 200
    assert response.json() == {
        "message": "Student created successfully", 
        "student": {"name": "John Doe", "email": "john.doe@example.com"}
    }

def test_create_student_empty_name():
    """Test creating a student with an empty name."""
    response = client.post("/students", json={"name": "", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_create_student_invalid_email():
    """Test creating a student with an invalid email."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity for email validation

def test_get_students():
    """Test retrieving all students."""
    response = client.get("/students")
    assert response.status_code == 200
    # Assert that the response contains a list of students and each has 'name' and 'email'
    students = response.json().get("students", [])
    assert isinstance(students, list)  # Check that 'students' is a list
    for student in students:
        assert "name" in student  # Each student record should contain a 'name'
        assert "email" in student  # Each student record should contain an 'email'