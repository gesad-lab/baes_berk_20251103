import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.models import Student  # Assuming your SQLAlchemy model is defined in src/models.py
from sqlalchemy.orm import Session
from src.database import get_db  # Assuming you have a dependency that provides a database session

@pytest.fixture
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def db_session():
    """Fixture to provide a database session for testing."""
    db = next(get_db())
    yield db
    # Here you can add code to tear down the database state if necessary

def test_create_student(client, db_session):
    """Test creating a new student."""
    response = client.post(
        "/students/",
        json={"name": "John Doe", "age": 20}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["age"] == 20

    # You may want to check that the student was added to the database
    student = db_session.query(Student).filter_by(name="John Doe").first()
    assert student is not None

def test_create_student_invalid_data(client):
    """Test creating a student with invalid data."""
    response = client.post(
        "/students/",
        json={"name": "", "age": -1}  # Example of invalid data
    )
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_student(client, db_session):
    """Test retrieving a student by ID."""
    student = Student(name="Jane Doe", age=22)  # Create a student instance
    db_session.add(student)
    db_session.commit()
    
    response = client.get(f"/students/{student.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"
    assert data["age"] == 22

def test_get_student_not_found(client):
    """Test retrieving a student that does not exist."""
    response = client.get("/students/999")  # Assuming 999 ID does not exist
    assert response.status_code == 404
    assert "detail" in response.json()

def test_get_students_list(client, db_session):
    """Test retrieving the list of students."""
    response = client.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Check if the response is a list
    # Optionally, check the contents of the list if needed
