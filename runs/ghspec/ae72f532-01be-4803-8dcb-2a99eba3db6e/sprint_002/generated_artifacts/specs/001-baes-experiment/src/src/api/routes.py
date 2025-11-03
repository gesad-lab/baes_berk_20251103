from flask import Blueprint, request, jsonify
from src.models.student import Student
from src.services.student_service import create_student, get_all_students

# Create a blueprint for our API routes
api = Blueprint('api', __name__)

@api.route('/students', methods=['POST'])
def create_student_route():
    """
    Create a new student with a name and email.
    
    Request JSON Body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    Returns:
        JSON response with created student data or error message.
    """
    # Parse the request JSON
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    name = data['name']
    email = data['email']

    # Here we would typically add more validation for email format 
    # but that is deferred to service layer for cleaner code.

    # Create the student using the service
    try:
        student = create_student(name=name, email=email)
    except Exception as e:
        # Log the exception (implementation of logging is not shown here)
        return jsonify({"error": {"code": "E002", "message": "Failed to create student.", "details": str(e)}}), 500

    # Return the created student data
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 201

@api.route('/students', methods=['GET'])
def retrieve_students():
    """
    Retrieve a list of all students with their names and emails.

    Returns:
        JSON response with a list of students.
    """
    try:
        students = get_all_students()
    except Exception as e:
        # Log the exception (implementation of logging is not shown here)
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve students.", "details": str(e)}}), 500

    # Format the response
    students_data = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    
    # Return the list of students
    return jsonify(students_data), 200