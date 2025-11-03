```python
from flask import Blueprint, request, jsonify
from models.student_course import StudentCourse  # Import the new StudentCourse model
from services.student_service import StudentService  # Assuming there is a service to handle business logic
from http import HTTPStatus

api = Blueprint('api', __name__)

@api.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve the list of courses a student is enrolled in.
    
    Args:
        student_id (int): The ID of the student to retrieve courses for.

    Returns:
        JSON response with a list of courses or an error message.
    """
    try:
        # Validate student_id format (additional validation can be done if necessary)
        if student_id <= 0:
            return jsonify({"error": {"code": "E001", "message": "Invalid student ID."}}), HTTPStatus.BAD_REQUEST
        
        # Fetch courses for the student via the service layer
        courses = StudentService.get_courses_by_student_id(student_id)

        if not courses:
            return jsonify({"message": "No courses found for this student."}), HTTPStatus.NOT_FOUND

        # Return the list of courses
        return jsonify(courses), HTTPStatus.OK

    except Exception as e:
        # Log error details for debugging (ensure that sensitive info is not logged)
        app.logger.error(f"Error retrieving courses for student {student_id}: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "An error occurred while retrieving courses."}}), HTTPStatus.INTERNAL_SERVER_ERROR
```