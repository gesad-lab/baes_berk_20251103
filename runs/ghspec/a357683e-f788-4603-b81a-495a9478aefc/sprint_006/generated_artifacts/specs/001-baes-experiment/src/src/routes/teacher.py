```python
from flask import Blueprint, request, jsonify
from app.models import Course, Teacher
from app import db

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/courses/<int:course_id>/remove-teacher', methods=['PATCH'])
def remove_teacher_from_course(course_id):
    """Remove a teacher from the specified course.

    Args:
        course_id (int): The ID of the course from which to remove the teacher.

    Returns:
        JSON response confirming the removal or an error message.
    """
    # Query the course by the provided course ID
    course = Course.query.get(course_id)

    # If the course does not exist, return a 404 error
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404

    # Remove the teacher by setting the teacher_id to None
    course.teacher_id = None

    # Commit the changes to the database
    db.session.commit()

    # Return a success response with the updated course data
    return jsonify({
        "message": "Teacher removed from course successfully.",
        "course_id": course.id,
        "teacher_id": course.teacher_id
    }), 200
```