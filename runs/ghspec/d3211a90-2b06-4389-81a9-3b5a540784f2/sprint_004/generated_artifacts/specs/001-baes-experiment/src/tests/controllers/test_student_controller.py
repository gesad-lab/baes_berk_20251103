```python
import pytest
from validation import validate_student_course_data

def test_validate_student_course_data_with_invalid_student_id():
    """
    Test case for validating student ID as invalid (non-integer).
    Expected outcome: ValueError should be raised indicating the student ID is invalid.
    """
    student_id = "abc"
    course_ids = [1, 2, 3]
    with pytest.raises(ValueError) as excinfo:
        validate_student_course_data(student_id, course_ids)

    assert str(excinfo.value) == "Invalid student ID."

def test_validate_student_course_data_with_invalid_course_ids():
    """
    Test case for validating course IDs as invalid (not a list of integers).
    Expected outcome: ValueError should be raised indicating course IDs must be a list of integers.
    """
    student_id = 1
    course_ids = "1, 2, 3"
    with pytest.raises(ValueError) as excinfo:
        validate_student_course_data(student_id, course_ids)

    assert str(excinfo.value) == "Course IDs must be a list of integers."

def test_validate_student_course_data_with_non_integer_course_ids():
    """
    Test case for validating course IDs containing non-integer values.
    Expected outcome: ValueError should be raised indicating course IDs must be a list of integers.
    """
    student_id = 1
    course_ids = [1, "two", 3]
    with pytest.raises(ValueError) as excinfo:
        validate_student_course_data(student_id, course_ids)

    assert str(excinfo.value) == "Course IDs must be a list of integers."

def test_validate_student_course_data_with_valid_data():
    """
    Test case for validating correct input for student ID and course IDs.
    Expected outcome: Function should not raise any exceptions.
    """
    student_id = 1
    course_ids = [1, 2, 3]
    try:
        validate_student_course_data(student_id, course_ids)
    except ValueError:
        pytest.fail("validate_student_course_data raised ValueError unexpectedly!")
```