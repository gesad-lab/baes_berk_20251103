```python
from flask import Blueprint, jsonify, request
from app import db
from app.models import Student
from email_validator import validate_email, EmailNotValidError

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student.
    
    This endpoint accepts a JSON body containing the student's name and email address to register a new student. 
    The email must be in a valid format.
    
    Request Body:
        - name (string): The name of the student (required).
        - email (string): The email address of the student (required, must be a valid format).
    
    Returns:
        - JSON with the created student's id, name, and email.
        - 201 Created on success.
        - 400 Bad Request with an error message if validation fails.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and email are required.'}}), 400

    # Validate email format
    try:
        validate_email(email)
    except EmailNotValidError as e:
        return jsonify({'error': {'code': 'E002', 'message': str(e)}}), 400

    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()

    return jsonify({'id': student.id, 'name': student.name, 'email': student.email}), 201

@students_bp.route('/students', methods=['GET'])
def get_students():
    """Retrieve the list of all students.
    
    This endpoint returns a JSON array of all registered students, including their names and email addresses.
    
    Returns:
        - JSON array of student objects, each containing id, name, and email.
    """
    students = Student.query.all()
    result = [{'id': student.id, 'name': student.name, 'email': student.email} for student in students]

    return jsonify(result), 200

@students_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student_email(student_id):
    """Update a student's email address.
    
    This endpoint updates the email address of a student identified by student_id.
    The new email must be in a valid format.
    
    Request Body:
        - email (string): The new email address of the student (required, must be a valid format).
    
    Returns:
        - JSON with confirmation of the updated email address.
        - 200 OK on success.
        - 400 Bad Request with an error message if validation fails or student does not exist.
    """
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': {'code': 'E001', 'message': 'Email is required.'}}), 400

    # Validate email format
    try:
        validate_email(email)
    except EmailNotValidError as e:
        return jsonify({'error': {'code': 'E002', 'message': str(e)}}), 400

    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E003', 'message': 'Student not found.'}}), 404

    student.email = email
    db.session.commit()

    return jsonify({'message': 'Email updated successfully.', 'email': student.email}), 200
```