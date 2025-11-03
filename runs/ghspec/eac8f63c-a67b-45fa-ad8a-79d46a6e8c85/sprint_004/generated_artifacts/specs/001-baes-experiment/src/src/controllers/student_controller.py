```python
import json
from flask import Blueprint, request, jsonify
from src.services.student_service import StudentService
from src.models.student import Student

student_controller = Blueprint('student_controller', __name__)
student_service = StudentService()

@student_controller.route('/students/<int:student_id>/courses', methods=['PATCH'])
def associate_course_to_student(student_id):
    """Handles associating a course with a student."""
    data = request.get_json()
    course_id = data.get('course_id')

    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "Course ID must be provided."}}), 400

    try:
        student_service.associate_course(student_id, course_id)
        return jsonify({"message": "Course associated successfully."}), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred."}}), 500

@student_controller.route('/students/<int:student_id>', methods=['GET'])
def get_student_info(student_id):
    """Retrieves student details along with their enrolled courses."""
    try:
        student = student_service.get_student_with_courses(student_id)
        return jsonify(student), 200
    except Student.DoesNotExist:
        return jsonify({"error": {"code": "E404", "message": "Student not found."}}), 404
    except Exception as e:
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred."}}), 500
```