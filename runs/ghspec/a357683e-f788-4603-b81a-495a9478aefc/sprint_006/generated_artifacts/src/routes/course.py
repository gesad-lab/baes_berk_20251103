```python
from flask import Blueprint, request, jsonify
from app import db
from app.models import Course, Teacher

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def retrieve_course(course_id):
    """
    Retrieve course details along with assigned teacher information.
    
    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        Response: JSON object containing course details and teacher's name or an error message.
    """
    # Attempt to find the course by ID
    course = Course.query.get(course_id)
    
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    # Prepare course data
    course_data = {
        "id": course.id,
        "name": course.name,
        "teacher": {
            "id": course.teacher.id if course.teacher else None,
            "name": course.teacher.name if course.teacher else "No teacher assigned"
        }
    }
    
    return jsonify(course_data), 200

# Register the blueprint in the application factory
def register_routes(app):
    app.register_blueprint(course_bp)
```