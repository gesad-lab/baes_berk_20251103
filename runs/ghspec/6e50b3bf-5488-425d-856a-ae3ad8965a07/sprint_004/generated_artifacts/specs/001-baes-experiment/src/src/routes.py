```python
from flask import Blueprint, jsonify, request
from src.models import Student, Course
from src.database import get_db_session

# Create a Blueprint for routes
bp = Blueprint('routes', __name__)

@bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Retrieve all courses associated with a given student by their ID.

    Args:
        student_id (int): The ID of the student whose courses are to be retrieved.

    Returns:
        JSON response with a list of enrolled courses or a message if none are found.
    """
    session = get_db_session()
    try:
        # Fetch the student from the database
        student = session.query(Student).filter(Student.id == student_id).first()
        
        # If student does not exist, return a 404 error
        if student is None:
            return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404
        
        # Retrieve courses associated with the student
        courses = student.courses  # Assuming a relationship is defined in the Student model
        
        # If no courses found, return a message indicating as such
        if not courses:
            return jsonify({"message": "No courses found for the student."}), 200
        
        # Return the list of courses
        return jsonify({"courses": [course.to_dict() for course in courses]}), 200  # to_dict() method should serialize the Course object

    except Exception as e:
        # Log the exception for debugging (not shown to the user)
        print(f"An error occurred while retrieving courses for student {student_id}: {e}")
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred."}}), 500
```