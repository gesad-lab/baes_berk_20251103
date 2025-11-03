```python
from flask import Blueprint, request, jsonify
from src.models.course_model import Course
from src.services.course_service import create_course, get_course, update_course

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/courses', methods=['POST'])
def create_course_route():
    """Handle course creation."""
    data = request.get_json()
    
    # Validate required fields
    name = data.get('name')
    level = data.get('level')
    
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Both 'name' and 'level' are required."}}), 400

    # Create the course
    new_course = create_course(name, level)
    return jsonify(new_course), 201

@course_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course_route(course_id):
    """Retrieve a course by its ID."""
    course = get_course(course_id)
    
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    return jsonify(course), 200

@course_routes.route('/courses/<int:course_id>', methods=['PUT'])
def update_course_route(course_id):
    """Update an existing course."""
    data = request.get_json()

    # Validate required fields
    name = data.get('name')
    level = data.get('level')
    
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Both 'name' and 'level' are required."}}), 400

    updated_course = update_course(course_id, name, level)

    if updated_course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    return jsonify(updated_course), 200
```