# Here is the updated content for the `src/routes.py` file:

from flask import Blueprint, request, jsonify
from .models import Student  # Assuming the Student model is defined in models.py
from . import db  # Assuming db is configured in a database.py file

# Create a blueprint for the student routes
student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student with name and email.
    
    Request body must include:
    - name: str
    - email: str
    
    Returns:
    - 201 Created on success with the created student data.
    - 400 Bad Request if email is missing or invalid.
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and email are required fields.'}}), 400

    new_student = Student(name=data['name'], email=data['email'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id, 'name': new_student.name, 'email': new_student.email}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session on error
        return jsonify({'error': {'code': 'E002', 'message': 'Failed to create student.', 'details': str(e)}}), 500

@student_routes.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all students including their email addresses.
    
    Returns:
    - 200 OK with a list of students in JSON format.
    """
    try:
        students = Student.query.all()  # Query to get all students
        student_list = [{'id': student.id, 'name': student.name, 'email': student.email} for student in students]
        return jsonify(student_list), 200
    except Exception as e:
        return jsonify({'error': {'code': 'E003', 'message': 'Failed to retrieve students.', 'details': str(e)}}), 500

@student_routes.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieve a specific student by their ID including their email.
    
    Parameters:
    - id: int - The ID of the student to retrieve.
    
    Returns:
    - 200 OK with the student data if found.
    - 404 Not Found if the student does not exist.
    """
    try:
        student = Student.query.get_or_404(id)  # Retrieve student by ID or throw 404
        return jsonify({'id': student.id, 'name': student.name, 'email': student.email}), 200
    except Exception as e:
        return jsonify({'error': {'code': 'E004', 'message': 'Student not found.', 'details': str(e)}}), 404