```python
# src/services/student_service.py

from flask import request, jsonify
from app.models import Student
from app import db
from sqlalchemy.exc import IntegrityError

def create_student():
    """
    Create a new student record.

    Request Body:
        - name (str): The name of the student.
        - email (str): The email of the student.

    Returns:
        - 201 Created with student details if successful.
        - 400 Bad Request if name or email is missing.
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify(error={"code": "E001", "message": "Email is required."}), 400

    name = data['name']
    email = data['email']

    if not email:
        return jsonify(error={"code": "E001", "message": "Email is required."}), 400

    new_student = Student(name=name, email=email)

    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify(id=new_student.id, name=new_student.name, email=new_student.email), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify(error={"code": "E002", "message": "Failed to create student."}), 400

def get_all_students():
    """
    Retrieve all student records.

    Returns:
        - 200 OK with a JSON array of student records.
    """
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200
```