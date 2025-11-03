```python
import pytest
from api.validators import validate_student_name

def test_validate_student_name_success():
    """Test that a valid student name passes the validation."""
    valid_name = "John Doe"
    assert validate_student_name(valid_name) is None  # No exception means valid

def test_validate_student_name_empty():
    """Test that an empty student name raises a validation error."""
    empty_name = ""
    with pytest.raises(ValueError) as excinfo:
        validate_student_name(empty_name)
    assert str(excinfo.value) == "Student name is required."

def test_validate_student_name_special_characters():
    """Test that special characters in the student name raise a validation error."""
    invalid_name = "John@Doe!"
    with pytest.raises(ValueError) as excinfo:
        validate_student_name(invalid_name)
    assert str(excinfo.value) == "Student name cannot contain special characters."

def test_validate_student_name_length():
    """Test that a name that is too short raises a validation error."""
    short_name = "A"  # Assuming the minimum length is more than 1
    with pytest.raises(ValueError) as excinfo:
        validate_student_name(short_name)
    assert str(excinfo.value) == "Student name must be at least 2 characters long."

def test_validate_student_name_validated_length():
    """Test that a valid long student name passes the validation."""
    valid_long_name = "A Very Long and Acceptable Student Name"
    assert validate_student_name(valid_long_name) is None  # No exception means valid
```