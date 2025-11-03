```python
# src/api/routes.py

from flask import Blueprint, request, jsonify, abort
from datetime import datetime
from models import Course, Teacher  # Import necessary models
from database import db

api = Blueprint('api', __name__)

@api.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """Assign a Teacher to a Course by course_id."""
    data = request.get_json()
    
    # Validate request body
    if 'teacher_id' not in data:
        return jsonify({"error": {"code": "E001", "message": "Missing 'teacher_id' in request body."}}), 400

    teacher_id = data['teacher_id']

    # Check if the Teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Invalid teacher_id: Teacher not found."}}), 400

    # Update Course with the teacher_id
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"message": "Teacher successfully assigned to course."}), 200

@api.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve Course details including associated Teacher information."""
    course = Course.query.get(course_id)
    
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    teacher_info = None
    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        if teacher:
            teacher_info = {
                "id": teacher.id,
                "name": teacher.name,
                "email": teacher.email
            }

    course_data = {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "teacher": teacher_info
    }

    return jsonify(course_data), 200
```