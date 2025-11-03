```python
from flask import Blueprint, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from models import Student, Course, StudentCourse  # Assuming these are already defined in models.py

student_course_api = Blueprint('student_course_api', __name__)
db = SQLAlchemy()

@student_course_api.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id):
    """Enroll a student in a course."""
    data = request.get_json()
    if not data or 'course_id' not in data:
        return jsonify({"error": {"code": "E400", "message": "Bad Request: 'course_id' is required."}}), 400

    course_id = data['course_id']
    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student:
        return jsonify({"error": {"code": "E404", "message": f"Student with ID {student_id} not found."}}), 404
    if not course:
        return jsonify({"error": {"code": "E404", "message": f"Course with ID {course_id} not found."}}), 404

    student_course = StudentCourse(student_id=student_id, course_id=course_id)
    db.session.add(student_course)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E500", "message": "Internal Server Error: Could not enroll student."}}), 500

    return jsonify({"message": "Student successfully enrolled in course."}), 201


@student_course_api.route('/students/<int:student_id>/courses', methods=['GET'])
def list_student_courses(student_id):
    """List all courses for a given student."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E404", "message": f"Student with ID {student_id} not found."}}), 404

    courses = db.session.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    result = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]

    return jsonify(result), 200


@student_course_api.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_student_from_course(student_id, course_id):
    """Remove a student from a course."""
    student_course = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not student_course:
        return jsonify({"error": {"code": "E404", "message": "Enrollment not found."}}), 404

    db.session.delete(student_course)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E500", "message": "Internal Server Error: Could not remove student from course."}}), 500

    return jsonify({"message": "Student successfully removed from course."}), 200
```