```python
# src/errors.py

class CourseNotFoundError(Exception):
    """Exception raised for errors in the input course ID."""
    
    def __init__(self, course_id: int):
        self.course_id = course_id
        self.message = f"Course ID {self.course_id} not found."
        super().__init__(self.message)

# Centralized error handling for course-related errors
def handle_course_not_found(course_id: int):
    """Handle the situation where a course ID is not found."""
    raise CourseNotFoundError(course_id)

# Flask error handler for CourseNotFoundError
from flask import jsonify

def register_error_handlers(app):
    """Register custom error handlers for the Flask application."""
    
    @app.errorhandler(CourseNotFoundError)
    def handle_course_not_found_error(error):
        response = {
            "error": {
                "code": "E404",
                "message": error.message,
                "details": {}
            }
        }
        return jsonify(response), 404
```