```python
from src.database import db
from src.models import Course, Teacher
from flask import request, jsonify, abort

def get_course_details(course_id):
    """Retrieve details of the course including assigned teacher information."""
    # Fetch the course from the database using the provided course_id
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        abort(404, description="Course not found")

    # Prepare the response structure
    response = {
        "course_id": course.id,
        "course_name": course.name,
        "course_level": course.level,
        "teacher": None
    }

    # If a teacher is assigned, add their details to the response
    if course.teacher_id:
        teacher = Teacher.query.filter_by(id=course.teacher_id).first()
        if teacher:
            response["teacher"] = {
                "teacher_id": teacher.id,
                "teacher_name": teacher.name,
                "teacher_email": teacher.email
            }

    return jsonify(response), 200

def assign_teacher_to_course(course_id):
    """Assign a teacher to a course based on course ID and teacher ID from the request."""
    # Validate and get the teacher_id from the request body
    data = request.get_json()
    teacher_id = data.get("teacher_id")

    if not teacher_id:
        abort(400, description="teacher_id is required")

    # Fetch the course from the database
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        abort(404, description="Course not found")

    # Fetch the teacher to ensure they exist
    teacher = Teacher.query.filter_by(id=teacher_id).first()
    if not teacher:
        abort(404, description="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    # Prepare and return the confirmation response
    return jsonify({
        "message": "Teacher assigned successfully",
        "course_id": course_id,
        "teacher_id": teacher_id
    }), 200
```