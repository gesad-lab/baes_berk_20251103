```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Student

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_client():
    with TestingSessionLocal() as session:
        # Create the database schema for the test
        from src.database import Base
        Base.metadata.create_all(bind=engine)
        yield TestClient(app)
        # Drop the database schema after tests
        Base.metadata.drop_all(bind=engine)

def test_create_student_with_valid_email(test_client):
    response = test_client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_with_empty_email(test_client):
    response = test_client.post("/students/", json={"name": "John Doe", "email": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": {"code": "E001", "message": "Email field is required."}}

def test_get_all_students(test_client):
    response = test_client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)
    for student in students:
        assert "email" in student

def test_update_student_email(test_client):
    # First, create a student to update
    response = test_client.post("/students/", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    student_id = response.json()["id"]
    
    # Update the student's email
    response = test_client.put(f"/students/{student_id}", json={"email": "new.email@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "new.email@example.com"

def test_delete_student_removes_email(test_client):
    # First, create a student to delete
    response = test_client.post("/students/", json={"name": "Mark Smith", "email": "mark.smith@example.com"})
    student_id = response.json()["id"]

    # Delete the student
    response = test_client.delete(f"/students/{student_id}")
    assert response.status_code == 204

    # Check if the student still exists
    response = test_client.get(f"/students/{student_id}")
    assert response.status_code == 404
```