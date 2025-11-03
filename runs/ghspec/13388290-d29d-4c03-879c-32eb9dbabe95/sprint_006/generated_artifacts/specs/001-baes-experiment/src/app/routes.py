```python
from flask import jsonify, request
from app import app, db
from app.models import Course, Teacher

@app.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['POST'])
def assign_teacher(course_id, teacher_id):
    """Assign a Teacher to a Course by their IDs.
    
    Parameters:
    - course_id: The ID of the course to which a teacher is being assigned.
    - teacher_id: The ID of the teacher to be assigned to the course.

    Returns:
    - JSON response with success message or error details.
    """
    course = Course.query.get(course_id)
    teacher = Teacher.query.get(teacher_id)

    if not course or not teacher:
        return jsonify(error={'code': 'E001', 'message': 'Invalid course or teacher ID.'}), 400

    # Assign teacher to the course
    course.teacher_id = teacher.id
    db.session.commit()

    return jsonify(message='Teacher assigned successfully.'), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve details of a specific Course, including Teacher's information.
    
    Parameters:
    - course_id: The ID of the course to retrieve.

    Returns:
    - JSON response with course details including Teacher info or error details.
    """
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return jsonify(error={'code': 'E002', 'message': 'Course not found.'}), 404

    # Constructing response with course and optional teacher information
    course_details = {
        "id": course.id,
        "name": course.name,
        "teacher": {
            "name": course.teacher.name,
            "email": course.teacher.email
        } if course.teacher else None
    }

    return jsonify(course=course_details), 200
```