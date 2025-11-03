from flask import Blueprint, jsonify, request
from models.student import Student
from app import db

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/api/v1/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieve a student by their ID.

    Parameters:
    - id (int): The ID of the student to retrieve.

    Returns:
    - JSON response containing the student's ID, name, and email, 
      or an error message if the student is not found.
    """
    student = Student.query.get(id)
    
    if student is None:
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404

    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    })

# Other route definitions remain unchanged.