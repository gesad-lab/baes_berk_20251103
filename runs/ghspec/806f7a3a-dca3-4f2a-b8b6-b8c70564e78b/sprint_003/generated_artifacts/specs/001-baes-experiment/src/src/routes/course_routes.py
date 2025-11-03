```python
from flask import request, jsonify, Blueprint
from schemas.course_schema import CourseSchema
from services.course_service import CourseService

course_routes = Blueprint('course_routes', __name__)

# Initialize CourseSchema for validation
course_schema = CourseSchema()

@course_routes.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with validated data."""
    # Validate incoming data against the schema
    errors = course_schema.validate(request.json)
    if errors:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": errors}}), 400

    course_data = request.json
    course = CourseService.create_course(course_data)
    return jsonify(course), 201  # Return the created course with a 201 status

@course_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve course details by ID."""
    course = CourseService.get_course(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
    return jsonify(course)  # Return the course details

@course_routes.route('/courses/<int:course_id>', methods=['PUT', 'PATCH'])
def update_course(course_id):
    """Update an existing course."""
    # Validate incoming data against the schema
    errors = course_schema.validate(request.json)
    if errors:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": errors}}), 400

    course_data = request.json
    updated_course = CourseService.update_course(course_id, course_data)
    if not updated_course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
    return jsonify(updated_course)  # Return the updated course details
```