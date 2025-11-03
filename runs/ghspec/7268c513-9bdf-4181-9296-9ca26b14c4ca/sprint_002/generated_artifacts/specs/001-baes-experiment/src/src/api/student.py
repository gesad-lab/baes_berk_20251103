```python
from flask import Blueprint, jsonify, request
from app import db
from app.models import Student  # Assuming the Student model is defined and has the necessary attributes

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
def get_all_students():
    """
    Get all students.
    
    Returns:
        JSON: A list of student records with id, name, and email fields.
    """
    # Query all students from the database
    students = Student.query.all()

    # Format the output to include id, name, and email
    student_list = [{
        "id": student.id,
        "name": student.name,
        "email": student.email  # Include the email field in the response
    } for student in students]

    return jsonify(student_list), 200

@student_bp.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student.

    Request Body:
        JSON: A JSON object containing name and email of the student.

    Returns:
        JSON: The created student details or an error message if input is invalid.
    """
    data = request.get_json()

    # Validate required fields
    if not data or 'name' not in data or 'email' not in data:
        missing_field = 'name' if 'name' not in data else 'email'
        return jsonify({"error": {"code": "E001", "message": f"{missing_field.capitalize()} is required."}}), 400

    # Create and save the new student
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "id": new_student.id,
        "name": new_student.name,
        "email": new_student.email
    }), 201
```