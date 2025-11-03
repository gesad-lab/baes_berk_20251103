import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.services.student_service import create_student
from src.repositories.student_repository import get_students

client = TestClient(app)

# Sample test data
valid_student_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

invalid_student_data_no_email = {
    "name": "Jane Doe",
}

invalid_student_data_invalid_email = {
    "name": "Jane Doe",
    "email": "not-an-email"
}


def test_create_student_with_valid_email():
    response = client.post("/students/", json=valid_student_data)
    assert response.status_code == 201  # 201 Created
    response_data = response.json()
    
    assert response_data["name"] == valid_student_data["name"]
    assert response_data["email"] == valid_student_data["email"]
    
    # Verify the student was added to the database
    students = get_students()
    assert len(students) > 0
    assert any(student.name == valid_student_data["name"] for student in students)


def test_create_student_without_email():
    response = client.post("/students/", json=invalid_student_data_no_email)
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Email field is required.",
            "details": {}
        }
    }


def test_create_student_with_invalid_email():
    response = client.post("/students/", json=invalid_student_data_invalid_email)
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Invalid email format.",
            "details": {}
        }
    }


def test_retrieve_all_students():
    response = client.get("/students/")
    assert response.status_code == 200  # 200 OK
    response_data = response.json()
    
    # Respond with list of students, ensure validity
    assert isinstance(response_data, list)
    for student in response_data:
        assert "name" in student
        assert "email" in student
        assert isinstance(student["name"], str)
        assert isinstance(student["email"], str)  # Email should be a string
```
