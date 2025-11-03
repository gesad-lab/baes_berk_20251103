```python
# src/services/course_service.py

from flask import jsonify
from sqlalchemy.exc import IntegrityError
from src.models.course import Course  # Assuming Course model is defined in this path
from src import db

def create_course(course_data):
    """
    Create a new course.
    
    Parameters:
    - course_data: A dictionary containing course information.
    
    Returns:
    - JSON response with course information or error details.
    """
    # Validate input data
    name = course_data.get('name')
    level = course_data.get('level')

    if not name or not level:
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Validation Error: Course name and level are required.',
                'details': {
                    'name': 'Field is required.' if not name else None,
                    'level': 'Field is required.' if not level else None
                }
            }
        }), 400  # Bad Request

    try:
        # Create a new Course instance
        new_course = Course(name=name, level=level)
        db.session.add(new_course)
        db.session.commit()
        
        # Return the created course information
        return jsonify(new_course.serialize()), 201  # Created
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'Database Error: Unable to create course.',
                'details': str(e.orig)  # Provide error details for debugging
            }
        }), 500  # Internal Server Error
        
def get_all_courses():
    """
    Retrieve all courses.
    
    Returns:
    - JSON response with list of courses.
    """
    courses = Course.query.all()
    return jsonify([course.serialize() for course in courses]), 200  # OK

def update_course_level(course_id, new_level):
    """
    Update the level of an existing course.
    
    Parameters:
    - course_id: The ID of the course to update.
    - new_level: The new level for the course.
    
    Returns:
    - JSON response with updated course information or error details.
    """
    if not new_level:
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Validation Error: Course level is required.'
            }
        }), 400  # Bad Request

    course = Course.query.get(course_id)
    if not course:
        return jsonify({
            'error': {
                'code': 'E003',
                'message': 'Not Found: Course does not exist.'
            }
        }), 404  # Not Found

    try:
        course.level = new_level
        db.session.commit()
        return jsonify(course.serialize()), 200  # OK
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'Database Error: Unable to update course level.',
                'details': str(e.orig)
            }
        }), 500  # Internal Server Error
```