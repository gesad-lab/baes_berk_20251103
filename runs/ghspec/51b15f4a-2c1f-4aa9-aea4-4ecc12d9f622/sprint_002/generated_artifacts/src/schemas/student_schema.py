```python
# src/controllers/student_controller.py

from flask import Blueprint, request, jsonify
from models.student import Student
from schemas.student_schema import StudentSchema
from app import db

student_blueprint = Blueprint('students', __name__)

@student_blueprint.route('/api/v1/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all students including their email addresses.
    
    Returns:
        Response: JSON representation of a list of students, each containing 
                  name and email, with a status code 200 OK.
    """
    students = Student.query.all()  # Fetch all students from the database
    student_schema = StudentSchema(many=True)  # Create a schema for serialization
    result = student_schema.dump(students)  # Serialize the list of students
    return jsonify(result), 200  # Return the serialized students as JSON


@student_blueprint.route('/api/v1/students', methods=['POST'])
def add_student():
    """
    Add a new student with name and email address.

    Returns:
        Response: JSON object with the added student's details including email, 
                  and status code 201 Created if successful.
                  Otherwise, returns status code 400 Bad Request.
    """
    student_data = request.json  # Get payload data in JSON format
    student_schema = StudentSchema()  # Create a schema for validation
    
    try:
        student = student_schema.load(student_data)  # Validate and deserialize input
    except Exception as e:
        return jsonify({'error': {'code': 'E001', 'message': str(e)}}), 400  # Handle validation error

    # If validation is successful, add the student to the database
    db.session.add(student)  # Add the student to the session
    db.session.commit()  # Commit the session to save changes
    
    return student_schema.dump(student), 201  # Return the added student


# Preserved existing structure and added the functionality to include email in responses.
```