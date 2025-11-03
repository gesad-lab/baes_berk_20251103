```python
import pytest
from validation import validate_course_data

def test_validate_course_data_without_name():
    """
    Test case for creating a course without a name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {'level': 'Beginner'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_without_level():
    """
    Test case for creating a course without a level.
    Expected outcome: ValueError should be raised indicating the level field is required.
    """
    data = {'name': 'Introduction to Programming'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_empty_name():
    """
    Test case for creating a course with an empty name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {'name': '', 'level': 'Beginner'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_empty_level():
    """
    Test case for creating a course with an empty level.
    Expected outcome: ValueError should be raised indicating the level field is required.
    """
    data = {'name': 'Introduction to Programming', 'level': ''}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_valid_data():
    """
    Test case for creating a course with valid data.
    Expected outcome: Should pass without raising any exceptions.
    """
    data = {
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }
    try:
        validate_course_data(data)
    except ValueError:
        pytest.fail("validate_course_data raised ValueError unexpectedly!")
```