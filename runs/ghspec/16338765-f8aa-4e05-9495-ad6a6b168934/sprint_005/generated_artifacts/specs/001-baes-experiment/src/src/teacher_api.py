```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust the import based on your actual project structure
from src.models import Teacher, TeacherCreate, TeacherResponse  # Import necessary data models
from sqlalchemy.orm import Session
from db_setup import SessionLocal

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    """Setup a new database session for tests."""
    session = SessionLocal()
    yield session
    session.close()

@pytest.fixture(scope="function", autouse=True)
def clear_teachers(db_session):
    """Clear teachers from DB before each test to ensure isolation."""
    db_session.query(Teacher).delete()
    db_session.commit()

def test_create_teacher_valid(db_session):
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

    # Verify the teacher is actually saved in the database
    teacher = db_session.query(Teacher).filter(Teacher.id == data["id"]).first()
    assert teacher is not None
    assert teacher.name == "John Doe"
    assert teacher.email == "john.doe@example.com"

def test_create_teacher_invalid_email(db_session):
    """Test creating a teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"

def test_get_teacher_valid(db_session):
    """Test retrieving a teacher's information."""
    # First, create a teacher to retrieve
    create_response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    teacher_id = create_response.json()["id"]

    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == teacher_id
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_get_teacher_not_found(db_session):
    """Test retrieving a non-existent teacher."""
    response = client.get("/teachers/999")  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.json()["detail"] == "Teacher not found"

def test_update_teacher_valid(db_session):
    """Test updating a teacher's information with valid data."""
    # Create a teacher to update
    create_response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    teacher_id = create_response.json()["id"]
    
    # Update the teacher's name
    update_response = client.post(f"/teachers/{teacher_id}", json={"name": "John Updated", "email": "john.doe@example.com"})
    assert update_response.status_code == 200
    
    # Verify that the name has been updated
    get_response = client.get(f"/teachers/{teacher_id}")
    assert get_response.json()["name"] == "John Updated"

def test_update_teacher_invalid_email(db_session):
    """Test updating a teacher with an invalid email format."""
    create_response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    teacher_id = create_response.json()["id"]

    response = client.post(f"/teachers/{teacher_id}", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"
```