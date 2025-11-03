```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db, get_db
from src.models.teacher import Teacher  # Import the Teacher model
from src.schemas.teacher import TeacherCreate  # Import the TeacherCreate schema
from sqlalchemy.orm import Session
from fastapi import HTTPException

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    # Initialize the database and create necessary migrations
    init_db()
    db = get_db()
    yield db
    db.close()

def test_add_new_teacher(test_client, db_session):
    # Scenario: Add a New Teacher
    response = test_client.post(
        "/teachers",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    
    assert response.status_code == 201  # Assert that the response status is 201 Created

    # Check that the teacher was actually added to the database
    teacher = db_session.query(Teacher).filter_by(email="john.doe@example.com").first()
    assert teacher is not None  # Ensure teacher exists in the DB
    assert teacher.name == "John Doe"  # Validate that the name is correct

def test_get_teacher_details(test_client, db_session):
    # Scenario: Retrieve Teacher Details
    # First add a teacher to retrieve
    teacher = Teacher(name="Jane Smith", email="jane.smith@example.com")
    db_session.add(teacher)
    db_session.commit()
    
    response = test_client.get(f"/teachers/{teacher.id}")
    
    assert response.status_code == 200  # Assert that the response status is 200 OK
    response_json = response.json()
    assert response_json['name'] == "Jane Smith"  # Validate name
    assert response_json['email'] == "jane.smith@example.com"  # Validate email

def test_create_teacher_with_invalid_data(test_client):
    # Scenario: Validate Teacher Creation with Invalid Data
    response = test_client.post(
        "/teachers",
        json={"name": "", "email": "missing.name@example.com"}  # Missing name
    )
    
    assert response.status_code == 400  # Assert that the response status is 400 Bad Request
    error_response = response.json()
    assert "error" in error_response  # Ensure error response is present
    assert error_response["error"]["code"] == "E002"  # Validate specific error code for missing fields
```

