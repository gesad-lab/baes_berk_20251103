```python
from flask import Blueprint, request, jsonify
from src.models import Course
from src.services.course_service import CourseService

# Initialize a new Blueprint for course related routes
course_bp = Blueprint('course', __name__)
course_service = CourseService()

@course_bp.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with the provided name and level."""
    data = request.get_json()
    
    # Validate required fields
    if not data or not all(key in data for key in ('name', 'level')):
        return jsonify({"error": {"code": "E001", "message": "Missing required fields: 'name' and 'level'."}}), 400
    
    # Create the course using the service layer
    course = course_service.create_course(data['name'], data['level'])
    
    return jsonify({
        'id': course.id,
        'name': course.name,
        'level': course.level
    }), 201

@course_bp.route('/courses/<int:id>', methods=['GET'])
def retrieve_course(id):
    """Retrieve a course by its ID."""
    course = course_service.get_course_by_id(id)
    
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404
    
    return jsonify({
        'id': course.id,
        'name': course.name,
        'level': course.level
    }), 200
```