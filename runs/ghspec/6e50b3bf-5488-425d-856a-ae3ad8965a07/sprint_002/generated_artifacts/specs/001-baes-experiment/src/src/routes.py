```python
from flask import Flask, request, jsonify, abort
from models import Student  # Assuming this imports the Student model
from database import db  # Assuming this handles the SQLAlchemy database instance
from schemas import StudentSchema  # Assuming this handles the validation schema for Student

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student with name and email.

    Request body:
    {
        "name": "string",
        "email": "string"
    }

    Response on success:
    {
        "id": "int",
        "name": "string",
        "email": "string"
    }

    Returns 400 Bad Request if name or email is missing.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="E001: Name and email are required fields.")

    # Extract fields from request
    name = data['name']
    email = data['email']
    
    # Create the student instance
    new_student = Student(name=name, email=email)

    # Save to the database
    db.session.add(new_student)
    db.session.commit()

    # Return the created student details
    return jsonify({'id': new_student.id, 'name': new_student.name, 'email': new_student.email}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a student by their ID.

    Returns:
    {
        "id": "int",
        "name": "string",
        "email": "string"
    }

    Returns 404 Not Found if the student does not exist.
    """
    student = Student.query.get(student_id)
    if not student:
        abort(404, description=f"E002: Student with ID {student_id} not found.")

    # Return student details in JSON format
    return jsonify({'id': student.id, 'name': student.name, 'email': student.email}), 200
```