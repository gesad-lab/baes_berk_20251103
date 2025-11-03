from flask import Blueprint, jsonify, request
from src.services.enrollment_service import get_courses_for_student
from flask_restful import Resource

# Define a blueprint for API routes
api_bp = Blueprint('api', __name__)

class StudentCourses(Resource):
    """Handles requests related to retrieving courses for a specific student."""
    
    def get(self, student_id):
        """Retrieve courses for a specific student by their ID.
        
        Args:
            student_id (int): The ID of the student.

        Returns:
            JSON: A list of courses the student is enrolled in, or an error message.
        """
        try:
            courses = get_courses_for_student(student_id)
            return jsonify(courses), 200
        except ValueError as ve:
            # Handle the case where the student ID is invalid
            return jsonify({"error": {"code": "E001", "message": str(ve)}}), 400
        except Exception as e:
            # General error handling
            return jsonify({"error": {"code": "E002", "message": "An error occurred while retrieving courses."}}), 500

# Add the new route for retrieving student courses
api_bp.add_url_rule('/students/<int:student_id>/courses', view_func=StudentCourses.as_view('student_courses') )