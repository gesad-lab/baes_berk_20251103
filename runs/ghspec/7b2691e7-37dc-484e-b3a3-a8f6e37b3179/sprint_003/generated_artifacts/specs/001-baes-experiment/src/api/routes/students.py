```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import Student, Course, db  # Importing Course model
from sqlalchemy.exc import IntegrityError

students_bp = Blueprint('students', __name__)

class StudentSchema(Schema):
    """Schema to validate student data, including a valid email format."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email())

class CourseSchema(Schema):
    """Schema to validate course data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    level = fields.Str(required=True)

@students_bp.route('/courses', methods=['POST'])
def create_course():
    """Endpoint to create a new Course record.
    
    Request Body:
        - name (str): The name of the course.
        - level (str): The level of the course.
    
    Returns:
        - JSON object containing the created course details if successful.
        - JSON error response if validation fails.
    """
    data = request.json
    try:
        # Validate and deserialize input data
        course_schema = CourseSchema()
        course = course_schema.load(data)
        
        # Create a new Course instance
        new_course = Course(**course)
        db.session.add(new_course)
        db.session.commit()
        
        return jsonify(course_schema.dump(new_course)), 201
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Validation Error", "details": err.messages}}), 400
    except IntegrityError as err:
        db.session.rollback()  # Rollback in case of integrity error
        return jsonify({"error": {"code": "E002", "message": "Database Integrity Error", "details": str(err)}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "Internal Server Error", "details": str(e)}}), 500

@students_bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Endpoint to retrieve a Course record by its identifier.
    
    Returns:
        - JSON object containing the course details if found.
        - JSON error response if course is not found.
    """
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": {"code": "E004", "message": "Course Not Found"}}), 404
    
    course_schema = CourseSchema()
    return jsonify(course_schema.dump(course)), 200
```