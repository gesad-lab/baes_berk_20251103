```python
from flask import Blueprint, request, jsonify, abort
from your_application.models import Course, db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course.
    
    Request payload must contain:
    - name: String (required)
    - level: String (required)

    Returns:
    - JSON response with success message and course details
    - 400 Bad Request if validation fails
    """

    data = request.get_json()

    # Validate input fields
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Missing required field: name"}}), 400
    if 'level' not in data or not data['level']:
        return jsonify({"error": {"code": "E002", "message": "Missing required field: level"}}), 400

    # Create a new course instance
    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)
    
    try:
        db.session.commit()
        return jsonify({"message": "Course created successfully", "course": {"name": new_course.name, "level": new_course.level}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Could not create course", "details": str(e)}}), 500

@courses_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """
    Retrieve a course by its ID.

    Returns:
    - JSON response with course details
    - 404 Not Found if the course does not exist
    """

    course = Course.query.get(id)
    if course is None:
        return jsonify({"error": {"code": "E004", "message": "Course not found"}}), 404

    return jsonify({"id": course.id, "name": course.name, "level": course.level})

@courses_bp.route('/courses', methods=['GET'])
def get_all_courses():
    """
    Retrieve a list of all courses.

    Returns:
    - JSON array of course details
    """
    
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses])
```