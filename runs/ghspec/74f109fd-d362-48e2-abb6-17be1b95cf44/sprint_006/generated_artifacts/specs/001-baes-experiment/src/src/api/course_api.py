from flask import Blueprint, jsonify, request
from http import HTTPStatus
from src.repositories.course_repository import CourseRepository

course_api = Blueprint('course_api', __name__)

@course_api.route('/api/v1/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """
    Retrieve course details along with the associated teacher's name and email.
    
    Args:
        course_id (int): The ID of the course to retrieve.
    
    Returns:
        JSON response with course details, including teacher information if assigned,
        or an error message if the course does not exist.
    """
    course_repo = CourseRepository()
    
    # Fetch the course with the teacher's information
    course = course_repo.get_course_with_teacher(course_id)
    
    if course is None:
        return jsonify({
            "error": {
                "code": "E404",
                "message": "Course not found."
            }
        }), HTTPStatus.NOT_FOUND
    
    # Prepare the course details for response
    course_details = {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher": {
            "name": course.teacher.name if course.teacher else None,
            "email": course.teacher.email if course.teacher else None,
        },
    }

    return jsonify(course_details), HTTPStatus.OK

# Register the blueprint in the main application file (not shown here) for routing.