```python
from flask import Blueprint, request, jsonify, abort
from app.models import Course, Teacher
from app import db

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>', methods=['PATCH'])
def update_course(course_id):
    """Update the course to assign a teacher.

    Args:
        course_id (int): The ID of the course to update.

    Returns:
        JSON: The updated course record.
    """
    # Retrieve the request data
    data = request.get_json()

    # Validate the input
    teacher_id = data.get('teacher_id')
    if teacher_id is not None and not isinstance(teacher_id, int):
        return jsonify({"error": {"code": "E001", "message": "Invalid teacher_id format. It must be an integer."}}), 400

    # Fetch the course from the database
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    # Update the teacher_id of the course if provided
    if teacher_id is not None:
        # Validate if the teacher exists
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404
        course.teacher_id = teacher_id

    # Commit changes to the database
    db.session.commit()

    # Return the updated course data
    return jsonify({
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "teacher_id": course.teacher_id
    }), 200
```