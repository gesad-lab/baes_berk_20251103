```python
from flask import Blueprint, request, jsonify
from src.models import Course  # Assuming a Course model exists
from src.database import db  # Assuming SQLAlchemy is used for database interactions

# Define a blueprint for the course routes
course_bp = Blueprint('courses', __name__)

@course_bp.route('/api/v1/courses', methods=['POST'])
def create_course():
    """
    Create a new course entity.

    Request JSON should contain:
    - name: Required string for the course name
    - level: Required string for the course level

    Returns:
    - 201 Created with a success message on successful creation
    - 400 Bad Request with an error message if validation fails
    """
    data = request.json

    name = data.get('name')
    level = data.get('level')

    if not name or not level:
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Both name and level are required.'
            }
        }), 400

    # Create a new Course record
    new_course = Course(name=name, level=level)

    try:
        db.session.add(new_course)  # Add new course to the session
        db.session.commit()  # Commit the session to save changes
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'Error while creating course: ' + str(e)
            }
        }), 500

    return jsonify({'message': 'Course record created successfully.'}), 201


@course_bp.route('/api/v1/courses', methods=['GET'])
def get_courses():
    """
    Retrieve a list of all courses.

    Returns:
    - 200 OK with a JSON array of course records.
    """
    courses = Course.query.all()  # Retrieve all courses from the database
    return jsonify([{'name': course.name, 'level': course.level} for course in courses]), 200
```