```python
# src/services/student_service.py

from src.models import Student
from flask import jsonify, request
from your_app import db  # make sure to replace with actual import paths

def create_student():
    """Create a new Student with name and email from the request."""
    data = request.get_json()

    # Validate input data
    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400

    # Create and save the new Student record
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.to_dict()), 201

def get_student_by_id(student_id):
    """Retrieve a Student by their unique identifier."""
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

    return jsonify(student.to_dict()), 200
```