# tests/test_teacher.py

import pytest
from fastapi import status
from src.models import Teacher
from src.database import SessionLocal

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from src.main import app
    return TestClient(app)

@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture
def setup_teachers(db_session):
    # This fixture can be used to create a test teacher in the database if needed
    teacher = Teacher(name="Test Teacher", email="test@school.com")
    db_session.add(teacher)
    db_session.commit()
    yield teacher
    db_session.delete(teacher)
    db_session.commit()

def test_create_teacher_success(client):
    # Test successful teacher creation
    response = client.post(
        "/teachers/",
        json={"name": "New Teacher", "email": "new@school.com"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "name": "New Teacher",
        "email": "new@school.com"
    }

def test_create_teacher_missing_name(client):
    # Test creation attempt without a name
    response = client.post(
        "/teachers/",
        json={"email": "missing_name@school.com"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required."
        }
    }

def test_create_teacher_missing_email(client):
    # Test creation attempt without an email
    response = client.post(
        "/teachers/",
        json={"name": "Missing Email"}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "error": {
            "code": "E002",  # Assuming we define this error code for missing email
            "message": "Email is required."
        }
    }