from flask import Blueprint, jsonify, request, abort
from src.models.student import Student
from src import db

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/students', methods=['GET'])
def get_students():
    """Retrieve all student records, including their names and emails."""
    students = Student.query.all()  # Query all students from the database
    result = []
    
    for student in students:
        # Append student details to the result list
        result.append({
            "id": student.id,
            "name": student.name,
            "email": student.email
        })
    
    return jsonify(result), 200  # Return student list as JSON with 200 status code

def validate_email(email):
    """Validate email format. Returns True if valid, False otherwise."""
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@student_controller.route('/students', methods=['POST'])
def create_student():
    """Create a new student record with a name and email."""
    data = request.get_json()
    
    # Validate input
    if 'name' not in data or 'email' not in data:
        abort(400, jsonify({"error": {"code": "E001", "message": "Missing required fields: name, email"}}))

    name = data['name']
    email = data['email']
    
    if not validate_email(email):
        abort(400, jsonify({"error": {"code": "E002", "message": "Invalid email format"}}))

    # Create a new student instance
    new_student = Student(name=name, email=email)
    
    db.session.add(new_student)  # Add student to the session
    db.session.commit()  # Commit the session to save to the database
    
    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201  # Return created student with 201 status code