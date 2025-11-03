```python
from flask import Blueprint, request, jsonify
from src.services.student_service import StudentService
from src.models.student import Student

student_api = Blueprint('student_api', __name__)
student_service = StudentService()

@student_api.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    try:
        data = request.get_json()
        name = data.get('name')

        # Basic validation
        if not name or not isinstance(name, str):
            return jsonify({"error": {"code": "E001", "message": "Invalid name format. Name is required and must be a non-empty string."}}), 400

        student = student_service.create_student(name)
        return jsonify(student.to_dict()), 201

    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": "An unexpected error occurred.", "details": str(e)}}), 500


@student_api.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all student records."""
    try:
        students = student_service.get_students()
        return jsonify([student.to_dict() for student in students]), 200

    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": "An unexpected error occurred.", "details": str(e)}}), 500
```