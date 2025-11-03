```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse
from src.models.teacher import Teacher  # Import the Teacher model
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)  # Clean up the database after tests

def test_create_teacher_success():
    """Test scenario: Create a Teacher"""
    response = client.post("/teachers/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {
        "id": response.json()["id"],  # The ID should be returned
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_create_teacher_missing_fields():
    """Test scenario: Validate Required Fields"""
    response = client.post("/teachers/", json={"name": ""})  # No email provided
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: email",
            "details": {}
        }
    }

def test_create_teacher_duplicate_email():
    """Test scenario: Create Teacher with duplicate email"""
    client.post("/teachers/", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    response = client.post("/teachers/", json={"name": "Another Doe", "email": "jane.doe@example.com"})  # Duplicate email
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email already exists",
            "details": {}
        }
    }

def test_retrieve_teacher():
    """Test scenario: Retrieve Teacher Information"""
    response = client.get("/teachers/1")  # Assuming this ID exists
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()

def test_preserve_existing_data():
    """Test scenario: Ensure existing student and course data remains intact"""
    response = client.post("/students/", json={"name": "Studious Student"})
    assert response.status_code == 201
    
    # Ensure students data can still be retrieved after adding a teacher
    response_students = client.get("/students/")
    assert response_students.status_code == 200
    assert len(response_students.json()) > 0  # There should be at least one student
```