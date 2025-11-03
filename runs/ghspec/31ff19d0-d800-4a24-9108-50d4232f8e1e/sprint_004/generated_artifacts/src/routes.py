```python
from flask import Blueprint, request, jsonify
from src.models import db, Student, Course, StudentCourse
from sqlalchemy.exc import IntegrityError

routes = Blueprint('routes', __name__)

@routes.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve all courses a specified student is enrolled in."""
    # Fetch the student from the database
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E001", "message": "Student not found."}}), 404

    # Get the courses associated with the student
    courses = StudentCourse.query.filter_by(student_id=student_id).all()
    course_details = []
    
    for student_course in courses:
        course = Course.query.get(student_course.course_id)
        if course:
            course_details.append({
                "course_id": course.id,
                "course_name": course.name,
                "level": course.level
            })

    return jsonify(course_details), 200

@routes.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id):
    """Enroll a student in a specified course."""
    request_data = request.get_json()
    course_id = request_data.get('courseId')

    # Validate input data
    if not course_id:
        return jsonify({"error": {"code": "E002", "message": "Course ID is required."}}), 400

    # Check if the student exists
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E001", "message": "Student not found."}}), 404

    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    # Enroll the student in the course
    student_course = StudentCourse(student_id=student_id, course_id=course_id)

    try:
        db.session.add(student_course)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Student is already enrolled in this course."}}), 400

    return jsonify({
        "message": "Enrollment successful.",
        "student": {
            "id": student.id,
            "name": student.name
        },
        "course": {
            "id": course.id,
            "name": course.name,
            "level": course.level
        }
    }), 201
```