```python
# src/routes.py

from flask import Blueprint, request, jsonify
from marshmallow.exceptions import ValidationError
from src.models import Course, Teacher  # Assuming Teacher model exists
from src.schemas import CourseSchema, TeacherSchema
from src.extensions import db  # Assuming you have a database extension defined
from typing import Optional

routes = Blueprint('routes', __name__)

@routes.route('/assign_teacher', methods=['POST'])
def assign_teacher_to_course():
    """Assign a teacher to a course by IDs."""
    data = request.get_json()

    # Input validation for presence and correct data types
    course_id = data.get('course_id')
    teacher_id = data.get('teacher_id')

    if not isinstance(course_id, int) or not isinstance(teacher_id, int):
        return jsonify({"error": {"code": "E001", "message": "Invalid course_id or teacher_id type. Must be integers."}}), 400

    # Validate course and teacher existence
    course = Course.query.get(course_id)
    teacher = Teacher.query.get(teacher_id)

    if course is None:
        return jsonify({"error": {"code": "E002", "message": f"Course with ID {course_id} does not exist."}}), 404
    
    if teacher is None:
        return jsonify({"error": {"code": "E003", "message": f"Teacher with ID {teacher_id} does not exist."}}), 404

    # Assign teacher to course
    course.teacher_id = teacher_id

    try:
        db.session.commit()
        return jsonify({"message": "Teacher successfully assigned to course."}), 200
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": {"code": "E004", "message": "Failed to assign teacher to course.", "details": str(e)}}), 500

@routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course_with_teacher(course_id: int):
    """Retrieve a course along with its assigned teacher details."""
    course = Course.query.get(course_id)

    if course is None:
        return jsonify({"error": {"code": "E002", "message": f"Course with ID {course_id} does not exist."}}), 404

    course_schema = CourseSchema()
    return jsonify(course_schema.dump(course)), 200
```