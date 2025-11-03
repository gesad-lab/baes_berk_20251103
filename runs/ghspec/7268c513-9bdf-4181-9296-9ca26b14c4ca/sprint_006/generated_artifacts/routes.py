```python
from flask import Blueprint, request, jsonify
from models.course import Course
from models.teacher import Teacher
from app import db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a course by updating the course's teacher_id."""
    data = request.get_json()
    teacher_id = data.get('teacher_id')
    
    # Validate the presence of the teacher_id
    if teacher_id is None:
        return jsonify({"error": {"code": "E001", "message": "Teacher ID is required."}}), 400

    # Check if the teacher exists
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher ID does not exist."}}), 400
    
    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course ID does not exist."}}), 404

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.session.commit()

    # Return the updated course details
    return jsonify({"id": course.id, "name": course.name, "level": course.level, "teacher_id": course.teacher_id}), 200
```