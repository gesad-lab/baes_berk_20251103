```python
import json
from flask import Blueprint, request, jsonify
from src.services import create_course, get_all_courses
from src.models import Course

# Blueprint for course management
course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['POST'])
def create_course_endpoint():
    """Endpoint to create a new course."""
    data = request.get_json()
    name = data.get('name')
    level = data.get('level')

    # Validate input
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Both 'name' and 'level' are required."}}), 400

    # Try to create the course
    try:
        course = create_course(name, level)
        return jsonify({"message": "Course created successfully.", "course": {"name": course.name, "level": course.level}}), 201
    except Exception as e:
        # Log error context (not printed for security reasons)
        return jsonify({"error": {"code": "E002", "message": "Failed to create course.", "details": str(e)}}), 500

@course_bp.route('/courses', methods=['GET'])
def retrieve_courses_endpoint():
    """Endpoint to retrieve all courses."""
    try:
        courses = get_all_courses()
        return jsonify([{"name": course.name, "level": course.level} for course in courses]), 200
    except Exception as e:
        # Log error context (not printed for security reasons)
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve courses.", "details": str(e)}}), 500
```