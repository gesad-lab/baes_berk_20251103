```python
# errors.py

"""
errors.py

This module centralizes error handling for the application.
It provides consistent JSON error messages for various failures,
including handling missing required course data.
"""

from flask import jsonify

def handle_missing_name():
    """ Handles missing name error for course creation. """
    response = {
        "error": {
            "code": "E002",
            "message": "Name is required.",
            "details": {}
        }
    }
    return jsonify(response), 400

def handle_missing_level():
    """ Handles missing level error for course creation. """
    response = {
        "error": {
            "code": "E003",
            "message": "Level is required.",
            "details": {}
        }
    }
    return jsonify(response), 400

def handle_course_not_found(course_id):
    """ Handles case where a course cannot be found by ID. """
    response = {
        "error": {
            "code": "E004",
            "message": f"Course with ID {course_id} not found.",
            "details": {}
        }
    }
    return jsonify(response), 404
```