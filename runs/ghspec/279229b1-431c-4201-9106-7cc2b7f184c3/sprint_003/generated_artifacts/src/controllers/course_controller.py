```python
# src/controllers/course_controller.py

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from your_app_name.models import Course, db  # Adjust according to your application structure

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course with the provided name and level.
    
    Request Body:
        {
            "name": "string",
            "level": "string"
        }
    
    Returns:
        JSON response with success message or error details.
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Both name and level are required."}}), 400

    name = data['name']
    level = data['level']

    # Create new Course instance
    new_course = Course(name=name, level=level)

    try:
        db.session.add(new_course)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Failed to create the course."}}), 500

    return jsonify({"message": "Course created successfully.", "course": {"name": new_course.name, "level": new_course.level}}), 201

@course_bp.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve a list of all existing courses.
    
    Returns:
        JSON response with a list of courses, including their name and level.
    """
    courses = Course.query.all()
    courses_list = [{"name": course.name, "level": course.level} for course in courses]

    return jsonify(courses_list), 200
```