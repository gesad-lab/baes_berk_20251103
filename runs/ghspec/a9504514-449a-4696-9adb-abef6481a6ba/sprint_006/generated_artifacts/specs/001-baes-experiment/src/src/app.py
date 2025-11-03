```python
from flask import Flask, jsonify, request, abort
from src.models import Course, Teacher
from src.database import db

app = Flask(__name__)

@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a specified course."""
    data = request.json

    # Validate request data
    if 'teacher_id' not in data:
        return jsonify({"error": {"code": "E001", "message": "Missing teacher_id in request"}}), 400

    teacher_id = data['teacher_id']
    
    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Check if the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found"}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    # Return updated course details
    return jsonify({
        "course_id": course.id,
        "course_name": course.name,
        "teacher_id": course.teacher_id,
        "teacher_name": teacher.name
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve course details including the assigned teacher's information."""
    course = Course.query.get(course_id)
    
    # Check if the course exists
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404

    # Prepare response with course details and teacher info
    response = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher_id": course.teacher_id,
        "teacher_name": course.teacher.name if course.teacher else None
    }

    return jsonify(response), 200
```