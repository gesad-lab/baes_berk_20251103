```python
from flask import Blueprint, jsonify, request
from src.models import db
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse  # Assuming a model for the junction table exists
from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__)

@api.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve all courses associated with a specific student."""
    # Validate student existence
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E404", "message": "Student not found."}}), 404
    
    # Retrieve courses for the student
    courses = db.session.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student.id).all()
    
    # Format and return course information
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    return jsonify({"courses": course_list}), 200

@api.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id):
    """Enroll a student in a course."""
    # Validate request data
    data = request.get_json()
    course_id = data.get('course_id')
    
    # Check if course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404
    
    # Attempt to associate the student with the course
    try:
        enrollment = StudentCourse(student_id=student_id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E400", "message": "Student already enrolled in this course."}}), 400

    return jsonify({"message": "Student enrolled in course successfully."}), 201

@api.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_student_from_course(student_id, course_id):
    """Remove a student from a course."""
    enrollment = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
    if enrollment is None:
        return jsonify({"error": {"code": "E404", "message": "Enrollment not found."}}), 404
    
    db.session.delete(enrollment)
    db.session.commit()

    return jsonify({"message": "Student removed from course successfully."}), 200
```