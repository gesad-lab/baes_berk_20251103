```python
# src/utils/validation.py

from flask import jsonify
from models import db, Student, Course, StudentCourse  # Assuming these models exist
from sqlalchemy.exc import IntegrityError

def validate_course_ids(course_ids):
    """
    Validate the list of course IDs provided for enrollment.
    
    Parameters:
        course_ids (list): A list of course IDs to validate.
    
    Returns:
        bool: True if all course IDs are valid, else False.
    """
    # Ensure course IDs are valid integers
    for course_id in course_ids:
        if not isinstance(course_id, int) or course_id <= 0:
            return False
    return True

def associate_courses_with_student(student_id, course_ids):
    """
    Associate the provided course IDs with the specified student.
    
    Parameters:
        student_id (int): The ID of the student to associate courses with.
        course_ids (list): The list of course IDs to associate.
    
    Returns:
        JSON response with the updated student information or error message.
    """
    # Validate course IDs
    if not validate_course_ids(course_ids):
        return jsonify({"error": {"code": "E001", "message": "Invalid course IDs provided."}}), 400

    # Retrieve student
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # Clear existing course associations
    student.courses = []

    # Associate new courses
    for course_id in course_ids:
        course = Course.query.get(course_id)
        if course:
            student.courses.append(course)
        else:
            return jsonify({"error": {"code": "E003", "message": f"Course ID {course_id} not found."}}), 404

    # Commit changes to the database
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Failed to associate courses with student."}}), 500

    # Return updated student information
    return jsonify({
        "student_id": student.id,
        "courses": [{"course_id": course.id, "course_name": course.name} for course in student.courses]
    }), 200

def get_courses_for_student(student_id):
    """
    Retrieve all courses associated with the specified student.
    
    Parameters:
        student_id (int): The ID of the student whose courses should be retrieved.
    
    Returns:
        JSON response with the list of associated courses or error message.
    """
    # Retrieve student with related courses
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    # List associated courses
    courses = [{"course_id": course.id, "course_name": course.name} for course in student.courses]
    return jsonify({"student_id": student.id, "courses": courses}), 200
```