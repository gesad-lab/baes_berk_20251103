```python
# src/controllers.py

from flask import jsonify, request
from src.models import Student, db
from src.validation import validate_student
from sqlalchemy.exc import SQLAlchemyError

def create_student():
    """Create a new student with a name and email."""
    data = request.get_json()

    # Validate the incoming student data
    validation_errors = validate_student(data)
    if validation_errors:
        return jsonify({"error": {"code": "E001", "message": "Validation error", "details": validation_errors}}), 400
    
    try:
        new_student = Student(name=data['name'], email=data['email'])
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify({
            "id": new_student.id,
            "name": new_student.name,
            "email": new_student.email
        }), 201

    except SQLAlchemyError as e:
        # Log the error for debugging (without exposing sensitive information)
        # Consider using a logging system instead of print for production code
        print(f"Database error occurred: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Internal Server Error"}}), 500


def retrieve_students():
    """Retrieve all students from the database."""
    try:
        students = Student.query.all()
        student_list = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
        return jsonify(student_list), 200

    except SQLAlchemyError as e:
        # Log the error for debugging (without exposing sensitive information)
        print(f"Database error occurred: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Internal Server Error"}}), 500
```