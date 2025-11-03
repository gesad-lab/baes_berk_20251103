```python
from flask import Blueprint, request, jsonify
from src.models import Teacher
from src.database import db
import re

teacher_controller = Blueprint('teacher_controller', __name__)

def is_valid_email(email: str) -> bool:
    """Check if the provided email has a valid format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@teacher_controller.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher profile."""
    data = request.get_json()

    # Validate input data
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    if not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Create and save teacher
    new_teacher = Teacher(name=name, email=email)

    try:
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
    except Exception as e:
        db.session.rollback()  # Rollback on error
        return jsonify({"error": {"code": "E003", "message": "Failed to create teacher.", "details": str(e)}}), 500

@teacher_controller.route('/teachers/<int:id>', methods=['GET'])
def get_teacher(id):
    """Retrieve a teacher's details by ID."""
    teacher = Teacher.query.get(id)

    if not teacher:
        return jsonify({"error": {"code": "E004", "message": "Teacher not found."}}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```