```python
from flask import Blueprint, request, jsonify
from your_application.models import db, Student  # Import the database and Student model
from sqlalchemy.exc import IntegrityError

students_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students, including their email."""
    try:
        students = Student.query.all()  # Query all students
        # Serialize the student data, including email
        student_data = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
        return jsonify(student_data), 200  # Return the student data with a success status
    except Exception as e:
        # Log error context for debugging (implement your logging here)
        return jsonify({"error": {"code": "E500", "message": "Internal Server Error", "details": str(e)}}), 500

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not email:
        # Create a clear error response for missing email
        return jsonify({"error": {"code": "E001", "message": "Email field is required"}}), 400

    if not name:
        return jsonify({"error": {"code": "E002", "message": "Name field is required"}}), 400

    new_student = Student(name=name, email=email)
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Student with this email already exists"}}), 400
    except Exception as e:
        # Log error context for debugging
        return jsonify({"error": {"code": "E500", "message": "Internal Server Error", "details": str(e)}}), 500

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's information by student ID."""
    student = Student.query.get(student_id)
    
    if not student:
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404

    student_data = {"id": student.id, "name": student.name, "email": student.email}
    return jsonify(student_data), 200
```