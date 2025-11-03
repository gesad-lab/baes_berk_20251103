```python
from flask import jsonify

def handle_teacher_not_found(teacher_id):
    """Handles the error when a teacher with the specified ID is not found.

    Args:
        teacher_id (int): The ID of the teacher not found.
    
    Returns:
        JSON response with error details and 404 status code.
    """
    response = {
        "error": {
            "code": "E404",
            "message": f"Teacher with ID {teacher_id} does not exist."
        }
    }
    return jsonify(response), 404

def handle_course_not_found(course_id):
    """Handles the error when a course with the specified ID is not found.

    Args:
        course_id (int): The ID of the course not found.
    
    Returns:
        JSON response with error details and 404 status code.
    """
    response = {
        "error": {
            "code": "E404",
            "message": f"Course with ID {course_id} does not exist."
        }
    }
    return jsonify(response), 404

def register_error_handlers(app):
    """Registers error handlers for the application.

    Args:
        app (Flask): The Flask application instance.
    """
    @app.errorhandler(404)
    def not_found_error(error):
        return handle_course_not_found(error.description)

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({"error": {"code": "E400", "message": "Bad request"}}), 400

    # Add any additional centralized error handlers as needed
```