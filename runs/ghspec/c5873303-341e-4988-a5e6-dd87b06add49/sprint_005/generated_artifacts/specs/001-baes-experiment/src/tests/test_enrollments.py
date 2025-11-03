```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Student, Course, StudentCourse  # import the models used
from src.database import get_db
from sqlalchemy.orm import sessionmaker

# Test client for the FastAPI application
client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    """Fixture that sets up a database session for testing."""
    db = get_db()
    yield db
    db.rollback()
    db.close()

@pytest.fixture(scope="module")
def create_dummy_student(db_session):
    """Fixture to create a dummy student for testing."""
    dummy_student = Student(name="Test Student", email="test@student.com")
    db_session.add(dummy_student)
    db_session.commit()
    yield dummy_student
    db_session.delete(dummy_student)
    db_session.commit()

@pytest.fixture(scope="module")
def create_dummy_course(db_session):
    """Fixture to create a dummy course for testing."""
    dummy_course = Course(title="Test Course")
    db_session.add(dummy_course)
    db_session.commit()
    yield dummy_course
    db_session.delete(dummy_course)
    db_session.commit()

def test_create_student(db_session, create_dummy_student):
    """Test case for creating a student."""
    response = client.post("/students/", json={"name": "New Student", "email": "new@student.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "New Student"
    assert data["email"] == "new@student.com"

def test_retrieve_students(db_session, create_dummy_student):
    """Test case for retrieving students."""
    response = client.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert any(student["email"] == "test@student.com" for student in data)

# Additional tests for the Teacher functionality.
def test_create_teacher():
    """Test case for creating a teacher."""
    response = client.post("/teachers/", json={"name": "Test Teacher", "email": "test@teacher.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Teacher"
    assert data["email"] == "test@teacher.com"

def test_retrieve_teachers():
    """Test case for retrieving teachers."""
    response = client.get("/teachers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Ensure response is a list format
```
