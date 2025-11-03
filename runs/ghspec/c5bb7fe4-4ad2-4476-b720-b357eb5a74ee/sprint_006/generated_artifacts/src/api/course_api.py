```python
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.models.course import Course  # Assuming the Course model is defined here
from src.models.teacher import Teacher  # Import the Teacher model
from src.services.course_service import assign_teacher_to_course, update_teacher_for_course
from sqlalchemy.exc import NoResultFound

course_api = Blueprint('course_api', __name__)
db = SQLAlchemy()

@course_api.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    """
    Assign a teacher to a course.
    
    Args:
        course_id (int): The ID of the course to assign the teacher to.
    
    Returns:
        response (json): JSON response with success message or error details.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    try:
        assign_teacher_to_course(course_id, teacher_id)
        return jsonify({"message": "Teacher assigned successfully."}), 200
    except NoResultFound:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Invalid teacher ID: The specified teacher does not exist.",
                "details": {}
            }
        }), 400  # Bad Request
    except Exception as e:
        # Generic error handling for unexpected issues
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500  # Internal Server Error


@course_api.route('/courses/<int:course_id>/update-teacher', methods=['PUT'])
def update_teacher(course_id):
    """
    Update the teacher assigned to a specific course.
    
    Args:
        course_id (int): The ID of the course to update.
    
    Returns:
        response (json): JSON response with success message or error details.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    try:
        update_teacher_for_course(course_id, teacher_id)
        return jsonify({"message": "Teacher updated successfully."}), 200
    except NoResultFound:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Invalid teacher ID: The specified teacher does not exist.",
                "details": {}
            }
        }), 400  # Bad Request
    except Exception as e:
        # Generic error handling for unexpected issues
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500  # Internal Server Error
```