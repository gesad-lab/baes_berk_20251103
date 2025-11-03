import pytest
from fastapi.testclient import TestClient
from main import app
from models import Student
from sqlalchemy.orm import Session
from database import get_db, Base, engine

# Create the test client used for sending requests to the application
client = TestClient(app)

# Dependency override for the database session
def override_get_db():
    db = Session(bind=engine)
    yield db
    db.close()

# Setup the test database and create the necessary tables
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Initialize the database and create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Tear down the database after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def student_data():
    return {"name": "John Doe", "email": "john.doe@example.com"}

def test_create_student(student_data):
    """Test creating a new student."""
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201
    assert response.json()["name"] == student_data["name"]
    assert response.json()["email"] == student_data["email"]

def test_get_student():
    """Test retrieving a student by ID."""
    # First create a student to test retrieval
    student_data = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    creation_response = client.post("/students/", json=student_data)
    student_id = creation_response.json()["id"]
    
    # Now attempt to retrieve the created student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == student_data["name"]
    assert response.json()["email"] == student_data["email"]

def test_update_student_email():
    """Test updating a student's email."""
    # Create a student first
    student_data = {"name": "Alice Smith", "email": "alice.smith@example.com"}
    creation_response = client.post("/students/", json=student_data)
    student_id = creation_response.json()["id"]

    new_email = {"email": "new.alice.smith@example.com"}
    response = client.put(f"/students/{student_id}/email", json=new_email)
    assert response.status_code == 200
    assert response.json()["email"] == new_email["email"]

def test_delete_student():
    """Test deleting a student."""
    # Create a student to delete
    student_data = {"name": "Bob Brown", "email": "bob.brown@example.com"}
    creation_response = client.post("/students/", json=student_data)
    student_id = creation_response.json()["id"]

    # Now delete the student
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204

    # Attempt to retrieve the deleted student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Not found after deletion