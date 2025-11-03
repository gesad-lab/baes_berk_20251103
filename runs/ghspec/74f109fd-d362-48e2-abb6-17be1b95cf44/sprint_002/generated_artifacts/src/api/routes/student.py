```python
from flask import Blueprint, request, jsonify
from src.repositories.student_repository import StudentRepository
from src.models.student import Student
from src.utils.email_validator import validate_email  # Assuming there's a utility for email validation
from http import HTTPStatus

student_bp = Blueprint('student', __name__)
student_repository = StudentRepository()

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student by ID, including name and email."""
    student = student_repository.find_by_id(student_id)
    
    if not student:
        return jsonify({"error": {"code": "E001", "message": "Student not found", "details": {}}}), HTTPStatus.NOT_FOUND

    # Return student details in JSON format
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    }), HTTPStatus.OK
```