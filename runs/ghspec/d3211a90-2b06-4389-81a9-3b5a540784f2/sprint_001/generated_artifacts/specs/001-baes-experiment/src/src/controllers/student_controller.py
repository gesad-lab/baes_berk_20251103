```python
from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from your_project.models import Student  # Assuming Student model is defined in models.py
from your_project.database import get_db  # Assuming a function to get the database session
from your_project.exceptions import InvalidUsage  # Custom exception for handling invalid requests

student_bp = Blueprint('student', __name__)

def validate_student_data(data):
    """Validate incoming student data."""
    if 'name' not in data or not data['name'].strip():
        raise ValueError("Name field is required.")

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    data = request.get_json()
    
    try:
        validate_student_data(data)  # Validate incoming data
        name = data['name'].strip()  # Get the name and ensure it is stripped of whitespace
        
        # Create a new student instance
        new_student = Student(name=name)
        
        # Get a new database session
        with get_db() as session:  # Ensure the session is closed after use
            session.add(new_student)  # Add the student to the session
            session.commit()  # Commit the transaction to save the new student
            student_id = new_student.id  # Get the ID of the newly created student
            
        # Return a success response with the student's ID and name
        return jsonify({"id": student_id, "name": name}), 201
    
    except ValueError as e:
        raise InvalidUsage(str(e), status_code=400)  # Handle validation error
    
    except Exception as e:
        # Log the exception and return an internal server error
        return jsonify({"error": "An unexpected error occurred."}), 500

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def retrieve_student(student_id):
    """Retrieve a student by ID."""
    with get_db() as session:  # Ensure the session is closed after use
        student = session.query(Student).filter(Student.id == student_id).first()  # Query for the student
        
        if student is None:
            return jsonify({"error": "Student not found."}), 404  # Not found response
        
        # Return the student's name in the response
        return jsonify({"name": student.name}), 200
```