```python
from flask import Blueprint, request, jsonify
from src.services.teacher_service import TeacherService
from src.models.teacher import Teacher
import re

teacher_api = Blueprint('teacher_api', __name__)
teacher_service = TeacherService()

def is_valid_email(email: str) -> bool:
    """Validate the email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

@teacher_api.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher."""
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Both name and email fields are required."}}), 400

    if not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    try:
        teacher = teacher_service.create_teacher(name, email)
        return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 201
    except ValueError as e:
        return jsonify({"error": {"code": "E003", "message": str(e)}}), 400
    except Exception as e:
        # Log the exception for debugging but don't expose details
        return jsonify({"error": {"code": "E004", "message": "An unexpected error occurred."}}), 500

@teacher_api.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve teacher information by ID."""
    teacher = teacher_service.get_teacher(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E005", "message": "Teacher not found."}}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```