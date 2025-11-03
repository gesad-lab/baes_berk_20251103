```python
# File: src/api/routes.py

from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from your_application.models import Student, Course, StudentCourse  # Adjust import based on your structure
from your_application.validators import validate_enrollment  # Importing validation function

api_bp = Blueprint('api', __name__)
db = SQLAlchemy()

@api_bp.route('/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    """
    Enroll a student in a course.

    Args:
        student_id (int): The ID of the student to enroll.
        request.json (dict): JSON containing `{"course_id": "Course ID"}`.

    Returns:
        JSON response with confirmation message or error message.
    """
    data = request.json
    if not data or 'course_id' not in data:
        return jsonify({"error": {"code": "E001", "message": "Course ID is required."}}), 400

    course_id = data['course_id']
    
    # Validate student_id and course_id
    validation_error = validate_enrollment(student_id, course_id)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    # Create an enrollment entry
    enrollment = StudentCourse(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Enrollment failed.", "details": str(e)}}), 500
    
    return jsonify({"message": "Student enrolled successfully."}), 201


@api_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """
    Retrieve the list of courses for a specific student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        JSON response with an array of courses or an error message.
    """
    courses = Course.query.join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    if not courses:
        return jsonify({"error": {"code": "E003", "message": "No courses found for this student."}}), 404

    # Map course data to a dictionary for response
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    
    return jsonify(course_list), 200
```