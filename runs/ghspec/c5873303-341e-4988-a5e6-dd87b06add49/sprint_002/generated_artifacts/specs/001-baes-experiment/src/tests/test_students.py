from fastapi import status
from fastapi.testclient import TestClient
import pytest
from src.main import app
from src.models import Student
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture
def test_db_session():
    # Assume this fixture provides a test database session
    pass

def test_create_student_with_email(test_db_session: Session):
    """Test successful creation of a student with email address."""
    response = client.post(
        "/students",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.json()
    created_student = test_db_session.query(Student).filter(Student.id == response.json()["id"]).first()
    assert created_student is not None
    assert created_student.name == "John Doe"
    assert created_student.email == "john.doe@example.com"

def test_create_student_missing_email(test_db_session: Session):
    """Test creation of a student fails when email is missing."""
    response = client.post(
        "/students",
        json={"name": "Jane Doe"}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"

def test_retrieve_all_students(test_db_session: Session):
    """Test retrieval of all students including email."""
    # Adding test data
    test_student = Student(name="Alice Smith", email="alice.smith@example.com")
    test_db_session.add(test_student)
    test_db_session.commit()

    response = client.get("/students")
    assert response.status_code == status.HTTP_200_OK
    students = response.json()
    assert len(students) > 0
    assert any(student['email'] == "alice.smith@example.com" for student in students)

def test_create_student_invalid_email_format(test_db_session: Session):
    """Test creation of a student fails when the email format is invalid."""
    response = client.post(
        "/students",
        json={"name": "Invalid Email", "email": "invalid-email"}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"