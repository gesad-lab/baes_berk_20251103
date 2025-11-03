```python
# src/routes/app_routes.py

from flask import Blueprint, request, jsonify
from src.controllers.course_controller import assign_teacher_to_course, get_courses_by_teacher
from src.models import Course, Teacher

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher():
    """
    Assign a teacher to a course.
    
    Parameters:
    - course_id (int): The ID of the course to which the teacher is being assigned.
    
    Request Body:
    - teacher_id (int): The ID of the teacher to be assigned.
    
    Returns:
    - JSON response indicating success or failure.
    """
    data = request.get_json()
    
    # Validate the input data
    if not data or 'teacher_id' not in data:
        return jsonify({"error": {"code": "E001", "message": "Missing teacher_id in the request body."}}), 400

    teacher_id = data['teacher_id']

    # Ensure the teacher exists before assigning
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404

    # Call the controller logic to assign the teacher to the course
    result = assign_teacher_to_course(course_id, teacher_id)
    
    if result.get('success'):
        return jsonify(result), 200
    return jsonify({"error": {"code": result.get('error_code', 'E003'), "message": result.get('message', "Failed to assign teacher.")}}), 500

@app_routes.route('/teachers/<int:teacher_id>/courses', methods=['GET'])
def courses_by_teacher(teacher_id):
    """
    Retrieve courses assigned to a specific teacher.
    
    Parameters:
    - teacher_id (int): The ID of the teacher.
    
    Returns:
    - JSON list of courses assigned to the teacher.
    """
    courses = get_courses_by_teacher(teacher_id)
    
    if not courses:
        return jsonify([]), 200
    
    return jsonify(courses), 200
```