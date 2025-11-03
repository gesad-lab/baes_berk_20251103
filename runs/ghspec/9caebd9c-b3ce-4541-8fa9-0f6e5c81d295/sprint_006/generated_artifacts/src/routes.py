```python
from flask import Blueprint, request, jsonify
from your_application import db, Course, Teacher  # Adjust import based on your structure
from your_application.validators import validate_teacher_id  # Assuming we have a validation function

routes = Blueprint('routes', __name__)

@routes.route('/courses/<int:course_id>/assign-teacher', methods=['PUT'])
def assign_teacher(course_id):
    """
    Assign a teacher to a specified course.

    Request Body:
    - teacher_id: ID of the teacher to assign

    Returns:
    - JSON confirmation message on success
    - JSON error message if the Teacher ID is invalid or missing
    """
    data = request.get_json()

    # Validate request body
    if not data or 'teacher_id' not in data:
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Missing required field: teacher_id',
                'details': {}
            }
        }), 400

    teacher_id = data['teacher_id']

    # Validate if the teacher ID is valid
    if not validate_teacher_id(teacher_id):
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'Invalid teacher_id provided',
                'details': {}
            }
        }), 400

    # Attempt to assign the teacher to the course
    course = Course.query.get(course_id)
    if not course:
        return jsonify({
            'error': {
                'code': 'E003',
                'message': 'Course not found',
                'details': {}
            }
        }), 404

    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({
        'message': 'Teacher assigned successfully',
        'course_id': course_id,
        'teacher_id': teacher_id
    }), 200

@routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve course information and assigned teacher details.

    Returns:
    - JSON object containing course details and associated teacher information.
    """
    course = Course.query.get(course_id)
    if not course:
        return jsonify({
            'error': {
                'code': 'E003',
                'message': 'Course not found',
                'details': {}
            }
        }), 404

    # Prepare course details along with teacher information
    course_data = {
        'id': course.id,
        'name': course.name,
        'teacher_id': course.teacher_id,
    }

    return jsonify(course_data), 200
```