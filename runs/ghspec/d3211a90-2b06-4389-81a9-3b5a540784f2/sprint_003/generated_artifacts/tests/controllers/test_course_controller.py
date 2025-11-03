```python
import pytest
from validation import validate_course_data

def test_validate_course_data_without_name():
    """
    Test case for creating a course without a name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {'level': 'beginner'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_without_level():
    """
    Test case for creating a course without a level.
    Expected outcome: ValueError should be raised indicating the level field is required.
    """
    data = {'name': 'Python 101'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_empty_name():
    """
    Test case for creating a course with an empty name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {'name': '', 'level': 'beginner'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_empty_level():
    """
    Test case for creating a course with an empty level.
    Expected outcome: ValueError should be raised indicating the level field is required.
    """
    data = {'name': 'Python 101', 'level': ''}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_invalid_name_type():
    """
    Test case for creating a course with an invalid data type for name.
    Expected outcome: ValueError should be raised indicating the name must be a string.
    """
    data = {'name': 123, 'level': 'beginner'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_validate_course_data_with_invalid_level_type():
    """
    Test case for creating a course with an invalid data type for level.
    Expected outcome: ValueError should be raised indicating the level must be a string.
    """
    data = {'name': 'Python 101', 'level': 456}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."
```