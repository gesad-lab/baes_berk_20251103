```python
import pytest
from validation import validate_student_data

def test_validate_student_data_without_name():
    """
    Test case for creating a student without a name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)
    
    assert str(excinfo.value) == "Name field is required."


def test_validate_student_data_with_empty_name():
    """
    Test case for creating a student with an empty name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {'name': '', 'email': 'test@example.com'}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)
    
    assert str(excinfo.value) == "Name field is required."


def test_validate_student_data_without_email():
    """
    Test case for creating a student without an email.
    Expected outcome: ValueError should be raised indicating the email field is required.
    """
    data = {'name': 'John Doe'}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Email field is required."


def test_validate_student_data_with_empty_email():
    """
    Test case for creating a student with an empty email.
    Expected outcome: ValueError should be raised indicating the email field is required.
    """
    data = {'name': 'John Doe', 'email': ''}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Email field is required."


def test_validate_student_data_with_invalid_email_format():
    """
    Test case for creating a student with an invalid email format.
    Expected outcome: ValueError should be raised indicating the email format is invalid.
    """
    data = {'name': 'John Doe', 'email': 'invalid-email'}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Invalid email format."


def test_validate_student_data_with_valid_email():
    """
    Test case for creating a student with a valid email.
    Expected outcome: No exception should be raised, indicating valid data.
    """
    data = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
    # No exception should be raised for valid input
    validate_student_data(data)
```