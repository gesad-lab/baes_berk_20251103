```python
from flask import Blueprint, jsonify, request
from src.models.course import Course  # Import the Course model
from app import db

# Create a blueprint for the course API.
course_api = Blueprint('course_api', __name__)

@course_api.route('/courses', methods=['GET'])
def retrieve_courses():
    """Retrieve a list of all courses with their names and levels.

    Returns:
        JSON response containing a list of courses.
    """
    try:
        courses = Course.query.all()  # Query all course entries from the database
        # Create a list of course data to return
        course_list = [{'name': course.name, 'level': course.level} for course in courses]
        return jsonify(course_list), 200  # Return the course data as JSON with a 200 OK status
    except Exception as e:
        # Log error message for debugging, do not return sensitive information
        return jsonify({'error': {'code': 'E500', 'message': 'An unexpected error occurred while retrieving courses.', 'details': str(e)}}), 500

# Register the blueprint in the application configuration (if not already registered in the main app file)
```