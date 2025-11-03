```python
# src/controllers/course_controller.py

from flask import Blueprint, request, jsonify
from src.models import Course, Teacher
from src.services.course_service import assign_teacher_to_course, get_course_details
from sqlalchemy.exc import IntegrityError

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>/assign-teacher', methods=['PATCH'])
def assign_teacher():
    """Assign a teacher to a specific course.

    Args:
        course_id (int): The ID of the course to which the teacher will be assigned.
    
    Request Body:
        {
            "teacherId": integer  # The ID of the teacher to be assigned
        }

    Returns:
        Response: JSON object confirming assignment or error message.
    """
    data = request.get_json()
    teacher_id = data.get('teacherId')

    if teacher_id is None:
        return jsonify({"error": {"code": "E001", "message": "teacherId is required"}}), 400

    try:
        course = assign_teacher_to_course(course_id, teacher_id)
        return jsonify({"message": "Teacher assigned successfully", "courseId": course.id, "teacherId": teacher_id}), 200
    
    except ValueError as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 400
    except IntegrityError:
        return jsonify({"error": {"code": "E003", "message": "Invalid courseId or teacherId"}}), 400

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def retrieve_course_details(course_id):
    """Retrieve detailed information about a course along with assigned teacher details.

    Args:
        course_id (int): The ID of the course to retrieve details about.

    Returns:
        Response: JSON object containing course details with teacher information if available.
    """
    course = get_course_details(course_id)

    if course is None:
        return jsonify({"error": {"code": "E004", "message": "Course not found"}}), 404

    course_info = {
        "courseId": course.id,
        "courseName": course.name,
        "level": course.level
    }

    if course.teacher_id:
        course_info["teacher"] = {
            "id": course.teacher.id,
            "name": course.teacher.name,
            "email": course.teacher.email
        }
    else:
        course_info["teacher"] = None  # Indicate no teacher assigned

    return jsonify(course_info), 200
```