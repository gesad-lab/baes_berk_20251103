```python
# src/controllers/course_controller.py

from flask import Blueprint, request, jsonify, abort
from your_app_name.models import Course, Teacher
from your_app_name import db

course_controller = Blueprint('course_controller', __name__)

@course_controller.route('/teachers/<int:teacher_id>/courses', methods=['GET'])
def get_courses_for_teacher(teacher_id):
    """
    Retrieve all courses associated with a specific teacher.

    Parameters:
    - teacher_id (int): The ID of the teacher whose courses are to be retrieved.

    Returns:
    - JSON response containing a list of courses associated with the teacher
      or an error message if the teacher does not exist.
    """
    # Fetch teacher to validate existence
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        # Return a 404 error if the teacher does not exist
        return jsonify({"error": {"code": "E002", "message": "Teacher not found"}}, 404

    # Query to retrieve courses associated with the teacher
    courses = Course.query.filter_by(teacher_id=teacher_id).all()
    
    # Serialize course data to JSON
    course_data = [{"id": course.id, "name": course.name} for course in courses]
    
    return jsonify(course_data), 200
```