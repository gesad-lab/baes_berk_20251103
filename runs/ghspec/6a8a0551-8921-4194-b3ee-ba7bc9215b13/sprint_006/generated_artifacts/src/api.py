```python
from flask import Flask, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from models import Course, Teacher
from api import db

app = Flask(__name__)

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve course information along with the associated teacher details.

    Args:
        id (int): The ID of the course to retrieve.

    Returns:
        JSON: Course details including teacher name and email.
    """
    course = Course.query.get(id)
    if course is None:
        abort(404, description="Course not found")

    teacher = Teacher.query.get(course.teacher_id) if course.teacher_id else None
    teacher_info = {
        "name": teacher.name,
        "email": teacher.email,
    } if teacher else None

    return jsonify({
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher": teacher_info,
    }), 200

@app.route('/courses/<int:id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(id):
    """Assign a teacher to a course.

    Args:
        id (int): The ID of the course to which the teacher will be assigned.

    Returns:
        JSON: Updated course information with assigned teacher.
    """
    course = Course.query.get(id)
    if course is None:
        abort(404, description="Course not found")

    data = request.get_json()
    teacher_id = data.get('teacher_id')
    if not teacher_id:
        abort(400, description="Teacher ID is required")

    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        abort(400, description="Teacher not found")

    course.teacher_id = teacher_id
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(500, description="Failed to assign teacher to course")

    return jsonify({
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher": {
            "name": teacher.name,
            "email": teacher.email,
        },
    }), 200
```