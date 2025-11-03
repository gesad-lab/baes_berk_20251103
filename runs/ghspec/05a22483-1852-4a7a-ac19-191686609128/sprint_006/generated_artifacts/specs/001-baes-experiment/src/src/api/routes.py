from flask import Blueprint, request, jsonify
from src.services.course_service import assign_teacher_to_course, get_course_details
from src.models import Course
from your_app import db  # ensure to replace with actual import paths

# Create a Blueprint for API routes
api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher():
    """
    Assign a teacher to a course.

    :param course_id: ID of the course to which the teacher will be assigned.
    :return: JSON response with success message or error details.
    """
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    if not teacher_id:
        return jsonify({"error": {"code": "E001", "message": "Teacher ID is required."}}), 400

    try:
        # Attempt to assign the teacher to the course
        result = assign_teacher_to_course(course_id, teacher_id)
        return jsonify({"success": True, "message": result}), 200
    except ValueError as e:
        # Handle case where the course does not exist
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": {"code": "E003", "message": "An error occurred while assigning the teacher."}}), 500

@api_routes.route('/courses/<int:course_id>', methods=['GET'])
def get_course():
    """
    Retrieve course information along with assigned teacher details.

    :param course_id: ID of the course to retrieve information for.
    :return: JSON response with course details and teacher information or error details.
    """
    try:
        course_details = get_course_details(course_id)
        return jsonify(course_details), 200
    except ValueError as e:
        # Handle case where the course does not exist
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": {"code": "E003", "message": "An error occurred while retrieving course details."}}), 500

# Register the blueprint with the main app (assuming app is defined elsewhere)
# app.register_blueprint(api_routes)