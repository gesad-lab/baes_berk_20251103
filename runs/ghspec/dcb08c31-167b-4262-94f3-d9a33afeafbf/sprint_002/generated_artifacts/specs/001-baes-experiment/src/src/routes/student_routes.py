```python
from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from .models import Student  # Assuming the Student model is defined in models.py

student_routes = Blueprint('student_routes', __name__)
db = SQLAlchemy()

@student_routes.route('/students', methods=['POST'])
def add_student():
    """Add a new student with name and email."""
    data = request.get_json()

    # Validate input
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    # Validate email format
    if '@' not in email or '.' not in email.split('@')[1]:
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201


@student_routes.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    student_list = [{"id": student.id, "name": student.name, "email": student.email} for student in students]

    return jsonify(student_list), 200

# Update API Contract Documentation
# Added a new field `email` to the Student entity that is returned in the JSON responses of both
# adding a new student and retrieving all students. Error responses now include
# detailed messages and relevant error codes for input validation failures.
```