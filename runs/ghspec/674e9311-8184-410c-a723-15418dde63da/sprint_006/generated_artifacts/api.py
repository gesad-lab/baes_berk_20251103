```python
from flask import Blueprint, request, jsonify
from src.models.course import Course  # Import the Course model
from src.models.teacher import Teacher  # Import the Teacher model
from sqlalchemy.exc import NotFound

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course_with_teacher(course_id: int):
    """Fetch course details along with assigned teacher information.

    Args:
        course_id (int): ID of the course to retrieve.

    Returns:
        Response: JSON containing course details and teacher information or error message.
    """
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404

    response = {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "teacher": None
    }

    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        if teacher:  # Ensure teacher exists
            response["teacher"] = {
                "id": teacher.id,
                "name": teacher.name,
                "email": teacher.email
            }

    return jsonify(response), 200

@course_bp.route('/courses/<int:course_id>/assign-teacher', methods=['PUT'])
def assign_teacher_to_course(course_id: int):
    """Assign a teacher to an existing course.

    Args:
        course_id (int): ID of the course to update.

    Returns:
        Response: JSON indicating success or error message.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Validate input
    if not isinstance(teacher_id, int):
        return jsonify({"error": {"code": "E400", "message": "Invalid teacher ID format"}}), 400

    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404

    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E404", "message": "Teacher not found"}}), 404

    # Assign teacher to course
    course.teacher_id = teacher_id

    # Commit changes to the database
    try:
        course.save()  # Assuming there's a save method to handle session commit
    except Exception as e:  # Catch any unexpected exceptions
        return jsonify({"error": {"code": "E500", "message": "Failed to assign teacher"}}), 500

    return jsonify({"message": "Teacher assigned successfully"}), 200
```