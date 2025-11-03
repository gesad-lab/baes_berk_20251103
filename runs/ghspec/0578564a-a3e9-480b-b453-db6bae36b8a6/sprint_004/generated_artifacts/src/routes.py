```python
from flask import request, jsonify, Blueprint
from src.models import db, Student, Course, StudentCourse  # Assuming StudentCourse is the junction model
from sqlalchemy.exc import IntegrityError

routes = Blueprint('routes', __name__)

@routes.route('/api/v1/enroll', methods=['POST'])
def enroll_student():
    """Enroll a student in a course."""
    data = request.get_json()

    student_id = data.get('student_id')
    course_id = data.get('course_id')

    # Validate input
    if not isinstance(student_id, int) or not isinstance(course_id, int):
        return jsonify({"error": {"code": "E001", "message": "Invalid student_id or course_id, both must be integers."}}), 400

    # Check if student exists
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student ID does not exist."}}), 404
    
    # Check if course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course ID does not exist."}}), 404

    # Enroll the student in the course
    try:
        enrollment = StudentCourse(student_id=student_id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Student is already enrolled in this course."}}), 409

    return jsonify({"message": "Student enrolled in course successfully"}), 200

@routes.route('/api/v1/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve courses associated with a specific student."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student ID does not exist."}}), 404

    courses = StudentCourse.query.filter_by(student_id=student_id).all()
    enrolled_courses = [{"course_id": course.course_id, "name": course.course.name} for course in courses]

    return jsonify({"student_id": student_id, "courses": enrolled_courses}), 200
```