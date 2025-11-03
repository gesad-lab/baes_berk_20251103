```python
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Course, Teacher  # Assuming these models are defined in models.py
from validations import validate_teacher_assignment  # Assuming this function exists for validation

db = SQLAlchemy()

@app.route('/api/v1/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    """Assign a teacher to a specific course.

    Args:
        course_id (int): The ID of the course to assign the teacher to.

    Returns:
        jsonify: A JSON response with confirmation or error message.
    """
    data = request.json
    teacher_id = data.get('teacher_id')

    # Validate teacher assignment
    validation_error = validate_teacher_assignment(teacher_id)
    if validation_error:
        return jsonify({'error': {'code': 'E001', 'message': validation_error}}), 400

    # Attempt to find the course
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': {'code': 'E002', 'message': 'Course not found'}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    
    try:
        db.session.commit()  # Commit the changes to the database
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': {'code': 'E003', 'message': 'Failed to assign teacher', 'details': str(e)}}), 500

    return jsonify({'message': f'Teacher assigned successfully to course ID {course_id}'}), 200
```