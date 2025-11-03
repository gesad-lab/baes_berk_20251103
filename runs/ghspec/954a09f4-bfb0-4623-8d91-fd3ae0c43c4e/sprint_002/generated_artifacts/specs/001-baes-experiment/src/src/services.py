```python
from flask import jsonify, request
from .models import Student
from .database import db

def create_student():
    """Create a new student and return their details including email.
    
    Request Body:
    - name: string (required)
    - email: string (required)
    
    Returns:
    - 201 Created with student details if successful
    - 400 Bad Request if email is missing
    """
    data = request.get_json()  # Get the JSON data from the request
    name = data.get('name')
    email = data.get('email')

    # Validate required fields
    if not email:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Email is required."
            }
        }), 400

    # Create a new student instance
    student = Student(name=name, email=email)
    
    # Add to the session and commit
    db.session.add(student)
    db.session.commit()
    
    # Return created student with ID, name, and email
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    }), 201

def get_student(student_id):
    """Retrieve a student by their ID and return their details including email.
    
    Returns:
    - 200 OK with student details if found
    - 404 Not Found if student does not exist
    """
    student = Student.query.get(student_id)
    
    if not student:
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Student not found."
            }
        }), 404

    # Return found student with ID, name, and email
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    }), 200
```