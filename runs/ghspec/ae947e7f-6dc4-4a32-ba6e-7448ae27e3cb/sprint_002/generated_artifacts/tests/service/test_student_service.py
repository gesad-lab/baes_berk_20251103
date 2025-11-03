```python
import pytest
from src.service.student_service import create_student, get_student_by_id
from src.model.student import Student
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from fastapi import HTTPException

@pytest.fixture
def db_session():
    # Create a new session for each test
    session = Session()
    yield session
    session.close()

def test_create_student_success(db_session):
    """Test creating a student with a valid name and email."""
    
    student_name = "John Doe"
    student_email = "john.doe@example.com"
    student = create_student(student_name, student_email)
    assert student.name == student_name
    assert student.email == student_email

def test_create_student_missing_email(db_session):
    """Test creating a student without providing an email."""
    
    student_name = "Jane Doe"
    with pytest.raises(HTTPException) as exc_info:
        create_student(student_name, "")
    
    assert exc_info.value.status_code == 400  # 400 Bad Request
    assert exc_info.value.detail == {"error": {"code": "E001", "message": "Email field is required."}}

def test_create_student_invalid_email_format(db_session):
    """Test creating a student with an invalid email format."""
    
    student_name = "Jake Doe"
    invalid_email = "jake.doe@invalid"
    with pytest.raises(HTTPException) as exc_info:
        create_student(student_name, invalid_email)
    
    assert exc_info.value.status_code == 400  # 400 Bad Request
    assert exc_info.value.detail == {"error": {"code": "E002", "message": "Invalid email format."}}
```