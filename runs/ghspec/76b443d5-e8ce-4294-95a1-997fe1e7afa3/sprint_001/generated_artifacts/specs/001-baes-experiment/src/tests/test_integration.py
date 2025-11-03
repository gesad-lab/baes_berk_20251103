import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_application.models import Base, Student  # Replace with your actual import
from your_application.main import app  # Replace with your actual import

DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for tests
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database and the tables
Base.metadata.create_all(bind=engine)

# Dependency override to use testing database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db  # Assume get_db is your dependency for DB session

client = TestClient(app)

@pytest.fixture(scope="module")
def test_student():
    """Fixture to set up a test student."""
    student_data = {"name": "John Doe"}
    response = client.post("/students/", json=student_data)  # Adjust endpoint as necessary
    yield response.json()  # Return student data for further tests
    # Optionally, add cleanup logic if required

def test_create_student():
    """Test creating a new student."""
    student_data = {"name": "Jane Doe"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201  # Assume created response code is 201
    assert "id" in response.json()  # Check if ID is returned
    assert response.json()["name"] == student_data["name"]  # Verify the name is correct

def test_retrieve_student(test_student):
    """Test retrieving an existing student's details."""
    student_id = test_student["id"]  # Get the student ID from the fixture
    response = client.get(f"/students/{student_id}/")  # Adjust endpoint as necessary
    assert response.status_code == 200  # Assume successful retrieval returns 200 OK
    assert response.json()["name"] == test_student["name"]  # Verify the name matches

def test_create_student_without_name():
    """Test creating a new student with no name."""
    student_data = {}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 400  # Assume bad request returns 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}  # Adjust as per your error handling

# Additional cleanup or configuration can be done here if necessary.