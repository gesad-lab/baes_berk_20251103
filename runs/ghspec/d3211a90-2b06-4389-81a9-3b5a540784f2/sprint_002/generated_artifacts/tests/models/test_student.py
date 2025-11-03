```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.student import Student
from src.database import Base
from validation import validate_student_data

def test_validate_student_data_with_email():
    """
    Test case for creating a student with a valid email.
    Expected outcome: Should pass without raising any exceptions.
    """
    data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    try:
        validate_student_data(data)
    except ValueError:
        pytest.fail("Validation raised ValueError unexpectedly!")

def test_validate_student_data_without_email():
    """
    Test case for creating a student without an email.
    Expected outcome: ValueError should be raised indicating the email field is required.
    """
    data = {
        'name': 'John Doe'
    }
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Email field is required."

def test_validate_student_data_with_empty_email():
    """
    Test case for creating a student with an empty email string.
    Expected outcome: ValueError should be raised indicating the email field is required.
    """
    data = {
        'name': 'John Doe',
        'email': ''
    }
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Email field is required."

def test_validate_student_data_with_invalid_email():
    """
    Test case for creating a student with an invalid email format.
    Expected outcome: ValueError should be raised indicating the email format is invalid.
    """
    data = {
        'name': 'John Doe',
        'email': 'invalid-email-format'
    }
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Invalid email format."
```