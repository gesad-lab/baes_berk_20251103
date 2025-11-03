import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_application.database import Base, get_db
from your_application.models import Student  # Adjust based on your project's structure
from your_application.api import app  # The FastAPI application instance

# Create a new SQLite database for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def cleanup_database():
    # Cleanup the database after tests complete
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_student():
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"

def test_get_student():
    # Creating a student to retrieve
    create_response = client.post("/students", json={"name": "Jane Doe"})
    student_id = create_response.json()["id"]

    # Now retrieve the student by ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "Jane Doe"

def test_update_student():
    # Create a student to update
    create_response = client.post("/students", json={"name": "Alice"})
    student_id = create_response.json()["id"]

    # Update the student's name
    response = client.put(f"/students/{student_id}", json={"name": "Alice Smith"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Smith"

def test_delete_student():
    # Create a student to delete
    create_response = client.post("/students", json={"name": "Bob"})
    student_id = create_response.json()["id"]

    # Delete the student
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204  # No content returned

    # Verify if the student was actually deleted
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Student should not be found

def test_create_student_without_name():
    response = client.post("/students", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }