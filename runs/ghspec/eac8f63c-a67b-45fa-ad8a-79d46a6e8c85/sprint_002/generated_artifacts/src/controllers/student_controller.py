```python
from flask import Blueprint, request, jsonify
from src.services.student_service import StudentService
from src.models.student import Student
from src.database import db

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/students', methods=['POST'])
def create_student():
    """Create a new student with their email address."""
    data = request.get_json()

    # Validate incoming request data
    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400

    # Create the student instance
    student = Student(name=name, email=email)

    try:
        # Use the student service to add the student
        StudentService.add_student(student)
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "Failed to create student.", "details": str(e)}}), 500

    return jsonify({"message": "Student created successfully.", "student_id": student.id}), 201
```