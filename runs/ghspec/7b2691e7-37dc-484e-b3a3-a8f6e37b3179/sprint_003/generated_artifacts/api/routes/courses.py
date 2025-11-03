```python
from flask import Blueprint, jsonify, request
from marshmallow import Schema, fields, ValidationError
from models import Course, db  # Assuming the Course model is in models.py
from sqlalchemy.exc import IntegrityError

courses_bp = Blueprint('courses', __name__)

class CourseSchema(Schema):
    """Schema to validate course data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)  # Name must be provided
    level = fields.Str(required=True)  # Level must be provided

course_schema = CourseSchema()

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course.

    Requires the presence of 'name' and 'level' in the request JSON.
    On success, returns a 201 Created status with the created course data.

    Response Codes:
        201 Created: Course successfully created.
        400 Bad Request: Missing 'name' or 'level'.
    """
    try:
        # Validate and deserialize incoming JSON data
        course_data = request.json
        course = course_schema.load(course_data)
        
        new_course = Course(name=course['name'], level=course['level'])
        db.session.add(new_course)
        db.session.commit()
        
        return jsonify(course_schema.dump(new_course)), 201

    except ValidationError as err:
        # Return validation errors if data is not as expected
        return jsonify({"error": {"code": "E001", "message": "Validation failed", "details": err.messages}}), 400

    except IntegrityError:
        # Handle database integrity errors (e.g., duplicate entries)
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Database integrity error"}}), 400

@courses_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """
    Retrieve a course by its ID.

    On success, returns a 200 OK status with the course data.

    Response Codes:
        200 OK: Course found.
        404 Not Found: Course not found.
    """
    course = Course.query.get(id)
    if course is None:
        return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404

    return jsonify({"name": course.name, "level": course.level}), 200
```