import pytest
from fastapi.testclient import TestClient
from src.services.student_service import app, list_students, create_student, update_student, delete_student

client = TestClient(app)

@pytest.fixture
def sample_student():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com"  # Updated to include the email field
    }

def test_create_student(sample_student):
    """Test successful student creation with valid data."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201
    assert response.json()["name"] == sample_student["name"]
    assert response.json()["email"] == sample_student["email"]

def test_get_student():
    """Test retrieving a Student by ID returns accurate data including the email."""
    # First, create a student to retrieve
    create_response = client.post("/students/", json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    student_id = create_response.json()["id"]

    # Now retrieve the student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

def test_update_student_email():
    """Test updating a Student's email reflects the change in the response."""
    # Create a student first
    create_response = client.post("/students/", json={
        "name": "Sam Smith",
        "email": "sam.smith@example.com"
    })
    student_id = create_response.json()["id"]

    # Update the student's email
    update_response = client.put(f"/students/{student_id}", json={
        "email": "sam.updated@example.com"
    })
    assert update_response.status_code == 200
    assert update_response.json()["email"] == "sam.updated@example.com"

def test_list_students():
    """Test listing all Students returns a proper list with emails."""
    # Create a few students first
    client.post("/students/", json={"name": "Student One", "email": "student.one@example.com"})
    client.post("/students/", json={"name": "Student Two", "email": "student.two@example.com"})

    # Now list all students
    response = client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)
    assert len(students) >= 2  # Assuming we created 2 students
    for student in students:
        assert "name" in student
        assert "email" in student  # Ensure each student has an email field