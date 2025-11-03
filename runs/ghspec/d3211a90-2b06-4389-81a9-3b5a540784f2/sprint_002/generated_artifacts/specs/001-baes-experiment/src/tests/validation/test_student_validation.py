```python
import pytest
from validation import validate_student_data

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
    Expected outcome: ValueError should be raised indicating invalid email format.
    """
    data = {'name': 'John Doe', 'email': 'invalid-email-format'}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)

    assert str(excinfo.value) == "Invalid email format."


def test_validate_student_data_with_valid_email():
    """
    Test case for creating a student with valid data.
    Expected outcome: No exception should be raised.
    """
    data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
    try:
        validate_student_data(data)  # Should pass without exceptions
    except ValueError:
        pytest.fail("validate_student_data raised ValueError unexpectedly!")
```