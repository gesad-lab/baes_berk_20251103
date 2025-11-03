```python
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.models.course import Course  # Assuming Course model exists
from src.models.teacher import Teacher  # Importing Teacher model
from src.services.course_service import assign_teacher_to_course, get_course_details  # Importing service functions
from sqlalchemy.exc import IntegrityError

courses_api = Blueprint('courses_api', __name__)
db = SQLAlchemy()

@courses_api.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher():
    """Assign a Teacher to a Course.
    
    Request payload should include:
    {
        "teacher_id": int
    }
    
    :param course_id: Course ID to which the teacher will be assigned.
    :return: JSON response with status and message.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')
    
    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Teacher ID is required."}}), 400

    try:
        assign_teacher_to_course(course_id, teacher_id)
        return jsonify({"message": "Teacher assigned successfully."}), 200
    except IntegrityError:
        db.session.rollback()  # Rollback the session on error
        return jsonify({"error": {"code": "E002", "message": "Invalid Course or Teacher ID."}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": str(e)}}), 500

@courses_api.route('/courses/<int:course_id>', methods=['GET'])
def get_course_with_teacher():
    """Retrieve Course details including assigned Teacher's name.
    
    :param course_id: the ID of the course to retrieve.
    :return: JSON object with course details and teacher's name.
    """
    course = get_course_details(course_id)
    
    if not course:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404
    
    response = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher_name": course.teacher.name if course.teacher else None  # Optional if no teacher assigned
    }
    
    return jsonify(response), 200
```