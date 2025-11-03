```python
# src/validation/course_validation.py

from flask import jsonify
from werkzeug.exceptions import BadRequest

def validate_course_creation(course_data):
    """
    Validate the creation of a new course.

    Parameters:
        course_data (dict): The course information containing 'name' and 'level'.

    Raises:
        BadRequest: If validation fails, raises with specific error message.

    Returns:
        None: Validation passed, returns nothing.
    """
    # Check if 'name' is present and not an empty string
    if 'name' not in course_data or not course_data['name'].strip():
        raise BadRequest('E001: Course name is required.')
    
    # Check if 'level' is present and not an empty string
    if 'level' not in course_data or not course_data['level'].strip():
        raise BadRequest('E002: Course level is required.')
    
    # Additional logic can be included here for further validations (e.g., length checks)

    # If all validations pass, return None
    return None
```