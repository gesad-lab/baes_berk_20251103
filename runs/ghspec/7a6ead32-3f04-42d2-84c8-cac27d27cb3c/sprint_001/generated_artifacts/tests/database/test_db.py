import pytest
from fastapi.testclient import TestClient
from main import app, get_database_connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

# Set up the test database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database schema
Base.metadata.create_all(bind=engine)

# Create a test client
client = TestClient(app)

@pytest.fixture
def db_session():
    """Fixture to provide a database session for tests."""
    db = SessionLocal()
    yield db
    db.close()

def test_create_student_valid(db_session):
    """Test creating a student with valid data."""
    response = client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"name": "John Doe", "id": 1}

def test_create_student_without_name():
    """Test creating a student without a name."""
    response = client.post("/students/", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_retrieve_existing_student():
    """Test retrieving an existing student."""
    # First create a new student
    client.post("/students/", json={"name": "Jane Doe"})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Jane Doe", "id": 1}

def test_retrieve_non_existing_student():
    """Test retrieving a non-existing student."""
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found"}}

def test_update_student_valid(db_session):
    """Test updating an existing student's name."""
    client.post("/students/", json={"name": "Old Name"})
    response = client.put("/students/1", json={"name": "Updated Name"})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Name", "id": 1}

def test_update_student_without_name():
    """Test updating a student without providing a name."""
    client.post("/students/", json={"name": "Another Old Name"})
    response = client.put("/students/1", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_delete_existing_student():
    """Test deleting an existing student."""
    client.post("/students/", json={"name": "Student to be deleted"})
    response = client.delete("/students/1")
    assert response.status_code == 204

def test_delete_non_existing_student():
    """Test deleting a non-existing student."""
    response = client.delete("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found"}}