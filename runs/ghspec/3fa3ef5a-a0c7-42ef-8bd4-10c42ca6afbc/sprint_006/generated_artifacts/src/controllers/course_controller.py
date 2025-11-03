```python
# src/controllers/course_controller.py

from flask import Blueprint, request, jsonify
from services.course_service import CourseService
from services.teacher_service import TeacherService
from models.course import Course
from models.teacher import Teacher

course_controller = Blueprint('course_controller', __name__)
course_service = CourseService()
teacher_service = TeacherService()

@course_controller.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """
    Retrieve the details of a specific course, including associated teacher information.

    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        JSON response containing course details and associated teacher information,
        or an error message if the course does not exist.
    """
    course = course_service.get_course_by_id(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404

    # Prepare the response with course details and teacher info if available
    course_details = {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher": {
            "id": course.teacher.id if course.teacher else None,
            "name": course.teacher.name if course.teacher else None,
        }
    }

    return jsonify(course_details), 200

@course_controller.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    """
    Assign a teacher to a specific course.

    Args:
        course_id (int): The ID of the course to which the teacher will be assigned.

    Returns:
        JSON response confirming the assignment or an error message if the teacher does not exist.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Validate input
    if not teacher_id:
        return jsonify({"error": {"code": "E400", "message": "Teacher ID must be provided."}}), 400

    # Check if teacher exists
    if not teacher_service.teacher_exists(teacher_id):
        return jsonify({"error": {"code": "E404", "message": "Teacher not found."}}), 404

    # Assign teacher to course
    result = course_service.assign_teacher(course_id, teacher_id)
    if not result:
        return jsonify({"error": {"code": "E500", "message": "Failed to assign teacher to course."}}), 500

    return jsonify({"message": "Teacher assigned successfully."}), 200

@course_controller.route('/courses/<int:course_id>/remove_teacher', methods=['DELETE'])
def remove_teacher_from_course(course_id):
    """
    Remove the teacher assignment from a specific course.

    Args:
        course_id (int): The ID of the course from which the teacher will be removed.

    Returns:
        JSON response confirming the removal or an error message if the operation fails.
    """
    result = course_service.remove_teacher(course_id)
    if not result:
        return jsonify({"error": {"code": "E500", "message": "Failed to remove teacher from course."}}), 500

    return jsonify({"message": "Teacher removed successfully."}), 200
```