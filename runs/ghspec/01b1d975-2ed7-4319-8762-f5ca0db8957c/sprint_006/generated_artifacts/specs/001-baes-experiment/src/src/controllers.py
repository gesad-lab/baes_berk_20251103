```python
# src/controllers.py

from flask import jsonify, request
from src.models import db, Course, Teacher
from src.validation import validate_teacher_exists, validate_course_exists

def retrieve_course_details(course_id: int):
    """Retrieve the details of a specific Course including its assigned Teacher."""
    
    # Validate the existence of the Course
    course = validate_course_exists(course_id)
    
    if not course:
        return jsonify({"error": {"code": "E001", "message": "Course not found."}}), 404
    
    # Prepare the response data
    course_details = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher": {
            "name": None,
            "email": None
        }
    }
    
    # Check if a Teacher is assigned
    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        if teacher:
            course_details["teacher"]["name"] = teacher.name
            course_details["teacher"]["email"] = teacher.email
            
    return jsonify(course_details), 200

def assign_teacher_to_course(course_id: int, teacher_id: int):
    """Assign a Teacher to a specific Course."""
    
    # Validate the existence of the Course and Teacher
    course = validate_course_exists(course_id)
    teacher = validate_teacher_exists(teacher_id)
    
    if not course:
        return jsonify({"error": {"code": "E001", "message": "Course not found."}}), 404
    
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Invalid Teacher ID."}}), 404
    
    # Assign the Teacher to the Course
    course.teacher_id = teacher.id
    db.session.commit()  # Persist the changes to the database

    return jsonify({
        "message": "Teacher assigned successfully.",
        "course_id": course.id,
        "teacher_id": teacher.id
    }), 200
```