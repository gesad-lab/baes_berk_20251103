```python
from flask import Flask, request, jsonify, abort
from models import Course, Teacher
from database import db

app = Flask(__name__)

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PATCH'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course to which the teacher is assigned.

    Returns:
        Response: JSON response indicating success or error.
    """
    # Get JSON data from the request
    data = request.get_json()

    # Validate request data
    if not data or 'teacher_id' not in data:
        return jsonify({'error': {'code': 'E003', 'message': 'Missing teacher_id in request body.'}}), 400

    teacher_id = data['teacher_id']

    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        abort(404, description='Course not found.')

    # Check if the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({'error': {'code': 'E002', 'message': 'Teacher not found.'}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id

    # Commit the changes to the database
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback session in case of error
        return jsonify({'error': {'code': 'E001', 'message': str(e)}}), 500

    return jsonify({
        'message': 'Teacher assigned to course successfully.',
        'course': {
            'id': course.id,
            'teacher_id': course.teacher_id
        }
    }), 200

# Other existing code...
```