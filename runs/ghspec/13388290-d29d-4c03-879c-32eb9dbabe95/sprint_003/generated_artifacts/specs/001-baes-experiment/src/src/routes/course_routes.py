```python
# File: src/routes/course_routes.py

from flask import Blueprint, request, jsonify
from app.models import Course
from app import db

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a course record by its ID.

    Args:
        id (int): The ID of the course to retrieve.

    Returns:
        JSON response containing course data or error message if not found.
    """
    course = Course.query.get(id)
    
    if not course:
        return jsonify(error={'code': 'E002', 'message': 'Course not found'}), 404

    return jsonify(id=course.id, name=course.name, level=course.level), 200
```