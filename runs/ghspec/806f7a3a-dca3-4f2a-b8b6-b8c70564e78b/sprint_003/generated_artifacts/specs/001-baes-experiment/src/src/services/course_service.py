```python
from flask import Blueprint, request, jsonify
from models.course import Course
from schemas.course_schema import CourseSchema
from extensions import db

course_blueprint = Blueprint('courses', __name__)

# Initialize a CourseSchema instance for validation
course_schema = CourseSchema()

@course_blueprint.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with the provided name and level."""
    json_data = request.get_json()
    
    # Validate incoming data
    errors = course_schema.validate(json_data)
    if errors:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": errors}}), 400
    
    course = Course(name=json_data['name'], level=json_data['level'])
    db.session.add(course)
    db.session.commit()
    
    return jsonify({"message": "Course created successfully", "course": course_schema.dump(course)}), 201


@course_blueprint.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve a course by its ID."""
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
    
    return jsonify({"course": course_schema.dump(course)}), 200


@course_blueprint.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update an existing course's name and level."""
    json_data = request.get_json()
    
    # Validate incoming data
    errors = course_schema.validate(json_data)
    if errors:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": errors}}), 400
    
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
    
    course.name = json_data.get('name', course.name)  # Update name if provided
    course.level = json_data.get('level', course.level)  # Update level if provided
    db.session.commit()
    
    return jsonify({"message": "Course updated successfully", "course": course_schema.dump(course)}), 200
```