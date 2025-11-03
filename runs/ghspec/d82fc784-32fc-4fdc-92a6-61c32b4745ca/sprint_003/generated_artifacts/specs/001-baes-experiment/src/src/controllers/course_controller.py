```python
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from app.models import Course
from app import db

course_controller = Blueprint('course_controller', __name__)

@course_controller.route('/courses', methods=['POST'])
def create_course():
    """Create a new course."""
    data = request.get_json()
    
    # Validate required fields
    if 'name' not in data or 'level' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Missing required fields: name, level'}}), 400
    
    try:
        # Create a new Course instance
        new_course = Course(name=data['name'], level=data['level'])
        db.session.add(new_course)
        db.session.commit()
        
        return jsonify({'message': 'Course created successfully', 'course_id': new_course.id}), 201
    except IntegrityError:
        db.session.rollback()  # Rollback the session in case of validation failure
        return jsonify({'error': {'code': 'E002', 'message': 'Course already exists'}}), 409
    except Exception as e:
        db.session.rollback()  # Rollback on any unexpected error
        return jsonify({'error': {'code': 'E003', 'message': 'An unexpected error occurred', 'details': str(e)}}), 500
        

@course_controller.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all courses."""
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name, 'level': course.level} for course in courses]), 200
```