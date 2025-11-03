```python
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from src.models import db, Course  # Importing the Course model

course_bp = Blueprint('course', __name__)

class CourseSchema(Schema):
    name = fields.Str(required=True)  # Validate that name is a required string
    level = fields.Str(required=True)  # Validate that level is a required string

course_schema = CourseSchema()

@course_bp.route('/courses', methods=['POST'])
def create_course():
    """Create a new course with a given name and level."""
    try:
        # Validate input data
        course_data = course_schema.load(request.json)
        
        # Create a new Course object
        new_course = Course(name=course_data['name'], level=course_data['level'])
        
        # Add the new course to the database
        db.session.add(new_course)
        db.session.commit()
        
        # Return a response with the new course details
        return jsonify({
            'id': new_course.id,
            'name': new_course.name,
            'level': new_course.level
        }), 201

    except ValidationError as err:
        # Handle validation errors and return appropriate response
        return jsonify({
            'error': {
                'code': 'E003',
                'message': 'Name and level are required.'
            }
        }), 400
    except Exception as e:
        # Catch unexpected errors and return a generic error response
        db.session.rollback()  # Rollback the session if there's an error
        return jsonify({
            'error': {
                'code': 'E500',
                'message': 'An unexpected error occurred.'
            }
        }), 500

@course_bp.route('/courses', methods=['GET'])
def list_courses():
    """Retrieve a list of all courses."""
    courses = Course.query.all()
    return jsonify([{
        'id': course.id,
        'name': course.name,
        'level': course.level
    } for course in courses]), 200
```