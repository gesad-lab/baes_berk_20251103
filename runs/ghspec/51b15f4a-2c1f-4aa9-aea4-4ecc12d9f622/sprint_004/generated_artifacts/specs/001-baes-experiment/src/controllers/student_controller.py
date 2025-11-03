```python
# controllers/student_controller.py

from flask import Blueprint, request, jsonify
from app import db
from models.enrollment import Enrollment
from models.student import Student
from models.course import Course

student_bp = Blueprint('student', __name__)

@student_bp.route('/enroll', methods=['POST'])
def enroll_student():
    """
    Enroll a student in one or more courses.

    Request JSON should contain:
        - student_id (int): The ID of the student to enroll.
        - course_ids (list): A list of course IDs to enroll the student in.

    Returns:
        - 200 OK: Successfully enrolled with details.
        - 400 Bad Request: If one or more course IDs are invalid.
    """
    data = request.get_json()

    student_id = data.get('student_id')
    course_ids = data.get('course_ids')

    # Validate input
    if not student_id or not course_ids:
        return jsonify({"error": {"code": "E001", "message": "Missing student_id or course_ids."}}), 400

    # Check if student exists
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Validate each course ID
    invalid_course_ids = []
    for course_id in course_ids:
        if not Course.query.get(course_id):
            invalid_course_ids.append(course_id)

    if invalid_course_ids:
        return jsonify({"error": {"code": "E003", "message": "Invalid course IDs provided.", "invalid_ids": invalid_course_ids}}), 400

    # Enroll the student in valid courses
    for course_id in course_ids:
        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        db.session.add(enrollment)

    db.session.commit()

    return jsonify({"message": "Successfully enrolled student.", "student_id": student_id, "course_ids": course_ids}), 200
```