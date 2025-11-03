from flask import Blueprint, request, jsonify
from models import Student, db

# Define a Blueprint for the student routes
student_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    # Validate request data
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    # Create a new student instance
    name = data['name']
    new_student = Student(name=name)

    # Add the new student to the database
    db.session.add(new_student)
    db.session.commit()

    # Return created student details with 201 Created status
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@student_bp.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    # Query all students from the database
    students = Student.query.all()

    # Map the student details to a list of dictionaries
    student_list = [{"id": student.id, "name": student.name} for student in students]

    # Return the list of students with 200 OK status
    return jsonify(student_list), 200