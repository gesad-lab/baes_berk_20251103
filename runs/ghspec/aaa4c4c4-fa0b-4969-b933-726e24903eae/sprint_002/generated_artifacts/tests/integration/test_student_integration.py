import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    """Fixture to create a student for testing purposes."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    return response.json()  # Return the created student data for further tests

def test_create_student_without_email():
    """Test creating a student without an email should fail."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required", "details": {}}}

def test_get_all_students(create_student):
    """Test retrieving all students includes the email field."""
    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()
    
    # Check that the student created in the fixture is present and includes the email field
    assert len(students) > 0
    assert any(student['email'] == create_student['email'] for student in students)
    assert 'name' in students[0]
    assert 'email' in students[0]

def test_create_student_success(create_student):
    """Test successfully creating a student and ensure the email field is saved."""
    assert create_student['name'] == "John Doe"
    assert create_student['email'] == "john.doe@example.com"