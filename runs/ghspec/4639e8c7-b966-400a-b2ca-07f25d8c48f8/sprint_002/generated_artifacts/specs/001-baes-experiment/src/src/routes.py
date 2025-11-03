```python
# File: src/routes.py

from flask import Blueprint, request, jsonify
from src.models import Student  # Assuming a Student model exists
from src.services import validate_email  # Importing a service function to validate emails
from src import db  # Importing the database to perform queries

bp = Blueprint('students', __name__)

@bp.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all student records, including email addresses.
    
    Returns:
        JSON response with all student records
    """
    students = Student.query.all()  # Fetching all students from the database
    student_records = [{
        'id': student.id,
        'name': student.name,
        'email': student.email  # Ensuring email is included in the response
    } for student in students]
    
    return jsonify(student_records), 200

@bp.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record with name and email.

    Returns:
        JSON response indicating success or failure
    """
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')

    # Input validation for name and email
    if not name:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required.'}}), 400

    if not email or not validate_email(email):
        return jsonify({'error': {'code': 'E002', 'message': 'Invalid email format.'}}), 400

    # Create a new student instance and add it to the database
    new_student = Student(name=name, email=email)
    
    try:
        db.session.add(new_student)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': {'code': 'E003', 'message': 'Failed to create student record.', 'details': str(e)}}), 500

    return jsonify({'message': 'Student created successfully', 'id': new_student.id}), 201
```