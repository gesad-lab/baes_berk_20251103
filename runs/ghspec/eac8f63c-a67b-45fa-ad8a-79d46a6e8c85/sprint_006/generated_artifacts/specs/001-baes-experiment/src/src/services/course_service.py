```python
# src/controllers/course_controller.py

from flask import Blueprint, request, jsonify
from src.services.course_service import CourseService
from src.models.course import Course
from src.models.teacher import Teacher

course_controller = Blueprint('course_controller', __name__)
course_service = CourseService()

@course_controller.route('/courses/<int:course_id>/assign_teacher', methods=['PUT'])
def assign_teacher_to_course(course_id):
    """Assign a teacher to a specified course."""
    teacher_id = request.json.get('teacher_id')

    # Validate input
    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Teacher ID is required."}}), 400

    # Call service to assign teacher to the course
    try:
        updated_course = course_service.assign_teacher(course_id, teacher_id)
        return jsonify(updated_course), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred."}}), 500

@course_controller.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """Retrieve course details including the assigned teacher's information."""
    try:
        course_details = course_service.get_course_with_teacher(course_id)
        return jsonify(course_details), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E003", "message": str(e)}}), 404
    except Exception as e:
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred."}}), 500
```