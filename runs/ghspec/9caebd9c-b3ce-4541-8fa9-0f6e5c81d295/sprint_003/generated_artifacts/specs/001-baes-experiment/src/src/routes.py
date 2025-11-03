```python
# src/validators.py

from flask import jsonify

def validate_course_input(course_data):
    """
    Validate the input data for course creation.

    Parameters:
        course_data (dict): The course data containing 'name' and 'level'.

    Returns:
        tuple: Returns a tuple containing a boolean indicating validity and an error message (if any).
    """
    name = course_data.get('name')
    level = course_data.get('level')

    # Check if 'name' is missing or empty
    if not name or not isinstance(name, str):
        return False, jsonify({"error": {"code": "E001", "message": "Course name is required and must be a string."}})

    # Check if 'level' is missing or empty
    if not level or not isinstance(level, str):
        return False, jsonify({"error": {"code": "E002", "message": "Course level is required and must be a string."}})

    return True, None
```