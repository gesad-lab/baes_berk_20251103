```python
from flask import jsonify, request, abort
from sqlalchemy.exc import IntegrityError
from .models import Course  # Assuming models are in a module named models
from .database import db  # Assuming database management is in a module named database

def validate_course_data(data):
    """
    Validate the input data for creating or updating a course.

    Parameters:
        data (dict): The input data to validate.

    Raises:
        ValueError: If the data is invalid.
    """
    if 'name' not in data or not isinstance(data['name'], str) or not data['name']:
        raise ValueError("Invalid data: 'name' is required and must be a non-empty string.")
    
    if 'level' not in data or not isinstance(data['level'], str) or not data['level']:
        raise ValueError("Invalid data: 'level' is required and must be a non-empty string.")

def create_course():
    """Create a new course with validated data from the request."""
    data = request.get_json()
    
    try:
        validate_course_data(data)
        new_course = Course(name=data['name'], level=data['level'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except ValueError as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Database integrity error."}}), 500

def update_course(course_id):
    """Update an existing course identified by course_id."""
    data = request.get_json()
    
    try:
        validate_course_data(data)
        course = Course.query.get(course_id)

        if course is None:
            return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

        course.name = data.get('name', course.name)  # Allow partial updates
        course.level = data.get('level', course.level)  # Allow partial updates
        db.session.commit()
        
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Database integrity error."}}), 500
```
