```python
# src/error_handling.py

from flask import jsonify
from werkzeug.exceptions import NotFound, BadRequest

# Custom error responses for course enrollment errors

def handle_course_not_found(course_id: int):
    """Handles cases where a course cannot be found."""
    response = {
        "error": {
            "code": "E404",
            "message": f"Course with ID {course_id} not found.",
            "details": {}
        }
    }
    return jsonify(response), 404

def handle_student_not_found(student_id: int):
    """Handles cases where a student cannot be found."""
    response = {
        "error": {
            "code": "E404",
            "message": f"Student with ID {student_id} not found.",
            "details": {}
        }
    }
    return jsonify(response), 404

def handle_invalid_enrollment(course_id: int, student_id: int):
    """Handles invalid enrollment attempts."""
    response = {
        "error": {
            "code": "E400",
            "message": f"Invalid enrollment request. Course ID {course_id} or Student ID {student_id} is invalid.",
            "details": {}
        }
    }
    return jsonify(response), 400

def handle_enrollment_success(student_id: int, course_id: int):
    """Handles successful enrollment in a course."""
    response = {
        "message": "Enrollment successful.",
        "enrollment": {
            "student_id": student_id,
            "course_id": course_id
        }
    }
    return jsonify(response), 201

def handle_removal_success(student_id: int, course_id: int):
    """Handles successful course removal from a student's record."""
    response = {
        "message": "Course removal successful.",
        "removal": {
            "student_id": student_id,
            "course_id": course_id
        }
    }
    return jsonify(response), 200
```