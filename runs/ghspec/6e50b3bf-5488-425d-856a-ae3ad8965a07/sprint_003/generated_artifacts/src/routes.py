```python
from flask import jsonify, request, abort
from src.models import Course  # Importing the Course model
from src.database import db  # Importing the database instance

def get_course(course_id):
    """Retrieve a course by ID.
    
    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        JSON response with course data or a 404 error.
    """
    # Attempt to retrieve the course from the database
    course = Course.query.get(course_id)
    if course is None:
        # Course not found, abort with 404
        abort(404, description="Course not found")

    # Return course data as JSON response
    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level
    }), 200

# Define routes related to courses (assuming Flask is set up with Blueprints)
from flask import Blueprint

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def retrieve_course(course_id):
    """Endpoint to retrieve a specific course by its ID."""
    return get_course(course_id)

# Note: Make sure to register this blueprint in your main application (app.py).
```