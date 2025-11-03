```python
from flask import Blueprint, jsonify, request, abort
from src.models import Course, Teacher
from src.database import get_db_session

# Create a new blueprint for routes
bp = Blueprint('course_routes', __name__)

@bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve course details along with associated teacher information."""
    session = get_db_session()
    course = session.query(Course).filter_by(id=course_id).first()

    if not course:
        abort(404, description="Course not found")

    # Prepare response with course and teacher details
    response = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher": {
            "name": course.teacher.name if course.teacher else None,
            "email": course.teacher.email if course.teacher else None
        }
    }

    return jsonify(response), 200

@bp.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a specified course."""
    session = get_db_session()
    data = request.get_json()

    if not data or 'teacher_id' not in data:
        abort(400, description="Invalid request: Teacher ID is required")

    teacher_id = data['teacher_id']
    course = session.query(Course).filter_by(id=course_id).first()
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()

    if not course:
        abort(404, description="Course not found")
    if not teacher:
        abort(404, description="Teacher not found")

    # Assign teacher to course
    course.teacher_id = teacher.id
    session.commit()

    # Prepare response with updated course details
    response = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher": {
            "name": teacher.name,
            "email": teacher.email
        }
    }

    return jsonify(response), 200
```