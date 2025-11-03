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
    data = {"name": ""}
    with pytest.raises(ValueError) as excinfo:
        validate_student_data(data)
    
    assert str(excinfo.value) == "Name field is required."


def test_validate_student_data_with_valid_name():
    """
    Test case for creating a student with a valid name.
    Expected outcome: No exception should be raised when name is provided.
    """
    data = {"name": "John Doe"}
    try:
        validate_student_data(data)
    except ValueError:
        pytest.fail("validate_student_data raised ValueError unexpectedly!")