import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import get_db, Base
from src.main import app, Student

# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Override the dependency to use the in-memory database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture
def create_student():
    """Fixture to create a student for tests."""
    student = Student(name="Test Student")
    return student

def test_create_student(create_student):
    """Test for creating a new student."""
    response = client.post("/students/", json={"name": create_student.name})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": create_student.name}

def test_create_student_invalid_name():
    """Test for creating a student with an invalid name."""
    response = client.post("/students/", json={"name": ""})  # Empty name
    assert response.status_code == 400
    assert "detail" in response.json()  # Check if an error detail is included

def test_get_students():
    """Test for retrieving the list of students."""
    client.post("/students/", json={"name": "Student One"})
    client.post("/students/", json={"name": "Student Two"})
    
    response = client.get("/students/")
    assert response.status_code == 200
    assert len(response.json()) == 2  # Two students should be returned

def test_get_student_by_id(create_student):
    """Test for retrieving a student by ID."""
    client.post("/students/", json={"name": create_student.name})
    response = client.get("/students/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": create_student.name}

def test_get_student_not_found():
    """Test for retrieving a student that does not exist."""
    response = client.get("/students/999/")
    assert response.status_code == 404
    assert "detail" in response.json()  # Check for error detail

def test_update_student(create_student):
    """Test for updating an existing student."""
    client.post("/students/", json={"name": create_student.name})
    response = client.put("/students/1/", json={"name": "Updated Student"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Student"}

def test_delete_student(create_student):
    """Test for deleting a student."""
    client.post("/students/", json={"name": create_student.name})
    response = client.delete("/students/1/")
    assert response.status_code == 204
    
    # Verify student is deleted
    response = client.get("/students/1/")
    assert response.status_code == 404  # Should return 404 after deletion