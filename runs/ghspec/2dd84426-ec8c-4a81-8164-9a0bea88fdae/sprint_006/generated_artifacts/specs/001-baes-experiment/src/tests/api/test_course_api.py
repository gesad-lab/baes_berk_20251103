```python
# src/services/course_service.py

from src.models.course import Course
from src.models.teacher import Teacher
from src.database import db
from http import HTTPStatus
from flask import jsonify

def assign_teacher_to_course(course_id: int, teacher_id: int):
    """
    Assign a teacher to a course.

    Parameters:
    - course_id (int): ID of the course to which the teacher will be assigned.
    - teacher_id (int): ID of the teacher being assigned to the course.

    Returns:
    - A JSON response indicating the result of the assignment operation.
    """

    # Validate course existence
    course = db.session.query(Course).filter(Course.id == course_id).first()
    if not course:
        return jsonify({"error": {"code": "E004", "message": "Course does not exist."}}), HTTPStatus.NOT_FOUND

    # Validate teacher existence
    teacher = db.session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        return jsonify({"error": {"code": "E005", "message": "Teacher does not exist."}}), HTTPStatus.NOT_FOUND

    # Assign teacher to course
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"message": "Teacher successfully assigned to course."}), HTTPStatus.OK
```