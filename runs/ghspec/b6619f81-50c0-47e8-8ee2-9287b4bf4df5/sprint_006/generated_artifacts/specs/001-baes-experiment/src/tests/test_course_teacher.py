```python
from flask import Flask, request, jsonify
from models import Course, Teacher  # Assuming models.py contains Course and Teacher classes
from repositories import CourseRepository  # Assuming repository for course interactions
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    """Assign a teacher to a course."""
    data = request.json
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Missing teacher_id in the request body."}}), 400

    try:
        course = CourseRepository.assign_teacher(course_id, teacher_id)
        return jsonify({"course_id": course.id, "teacher_id": teacher_id}), 200
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Course not found or teacher ID is invalid."}}), 404

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve detailed information about a course, including the assigned teacher."""
    course = CourseRepository.get_course_with_teacher(course_id)

    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course not found."}}), 404

    return jsonify({
        "course_id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher": {
            "teacher_id": course.teacher.id,
            "name": course.teacher.name,
            "email": course.teacher.email
        } if course.teacher else None
    }), 200

@app.route('/courses/<int:course_id>/update-teacher', methods=['PUT'])
def update_teacher(course_id):
    """Update assigned teacher for a specific course."""
    data = request.json
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Missing teacher_id in the request body."}}), 400

    try:
        course = CourseRepository.update_teacher(course_id, teacher_id)
        return jsonify({"course_id": course.id, "teacher_id": teacher_id}), 200
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Course not found or teacher ID is invalid."}}), 404

# Ensure to implement the CourseRepository methods for assign_teacher, get_course_with_teacher, and update_teacher
```