```python
from flask import Blueprint, request, jsonify
from src.models import Student
from src.database import db
from sqlalchemy.exc import IntegrityError

bp = Blueprint('students', __name__)

@bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    # Validate input
    data = request.get_json()
    
    if not data:
        return jsonify({"error": {"code": "E001", "message": "Invalid JSON body."}}), 400
    
    # Check for required fields
    name = data.get('name')
    email = data.get('email')
    
    if not name or not isinstance(name, str):
        return jsonify({"error": {"code": "E002", "message": "Invalid or missing name."}}), 400
    
    if not email or not isinstance(email, str):
        return jsonify({"error": {"code": "E003", "message": "Email is a required field."}}), 400

    # Create student
    student = Student(name=name, email=email)

    try:
        db.session.add(student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({"error": {"code": "E004", "message": "Email must be unique."}}), 400

    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 201
```