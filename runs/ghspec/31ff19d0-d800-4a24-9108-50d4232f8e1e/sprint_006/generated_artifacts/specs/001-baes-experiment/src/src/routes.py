```python
from flask import Blueprint, request, jsonify, abort
from src.models import Course, Teacher, db  # Import the required models and db
from sqlalchemy.exc import SQLAlchemyError

routes = Blueprint('routes', __name__)

@routes.route('/courses/<int:courseId>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(courseId):
    """Assign a teacher to a course by courseId."""
    # Retrieve request data
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "teacher_id is required"}}), 400

    # Validate that the course exists
    course = Course.query.get(courseId)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Validate that the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found"}}), 404

    try:
        # Assign teacher to the course
        course.teacher_id = teacher_id
        db.session.commit()  # Persist the change to the database
    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back in case of error
        return jsonify({"error": {"code": "E004", "message": "Database error while assigning teacher", "details": str(e)}}), 500

    return jsonify({"message": "Teacher assigned successfully", "courseId": courseId, "teacherId": teacher_id}), 200


@routes.route('/courses/<int:courseId>', methods=['GET'])
def get_course_details(courseId):
    """Retrieve course details including assigned teacher information."""
    course = Course.query.get(courseId)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Prepare response data, including teacher info if assigned
    response_data = {
        "course_id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher_id,
        "teacher_name": (course.teacher.name if course.teacher else None),
        "teacher_email": (course.teacher.email if course.teacher else None),
    }

    return jsonify(response_data), 200
```