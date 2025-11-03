```python
# This file should contain the student controller functionalities
from flask import Blueprint, request, jsonify
from src.models.student import Student
from src.services.student_service import create_student, get_all_students

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['POST'])
def add_student():
    """Create a new student record."""
    data = request.get_json()
    name = data.get('name')

    if not name or len(name) < 1:
        return jsonify({"error": {"code": "E001", "message": "Invalid student name", "details": {}}}), 400

    student = create_student(name)
    return jsonify({"id": student.id, "name": student.name}), 201

@student_bp.route('/students', methods=['GET'])
def retrieve_students():
    """Retrieve all student records."""
    students = get_all_students()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200
```