```python
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.models import Student

routes = Blueprint('routes', __name__)
db = SQLAlchemy()

@routes.route('/students', methods=['POST'])
def create_student():
    """Create a new student entry in the database."""
    # Get JSON data from request
    data = request.get_json()

    # Input Validation
    if not data:
        return jsonify({"error": {"code": "E001", "message": "Request body cannot be empty."}}), 400

    name = data.get('name')
    email = data.get('email')  # Email validation will be implemented in future iterations

    # Validate name field
    if not name:
        return jsonify({"error": {"code": "E002", "message": "Name is required."}}), 400

    # Optionally, validate email format here when implemented in future
    # if email and not is_valid_email(email):
    #     return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create and save the student object
    new_student = Student(name=name, email=email)
    try:
        db.session.add(new_student)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": f"Failed to create student: {str(e)}"}}), 500

    return jsonify({"message": "Student created successfully", "student": {"id": new_student.id, "name": new_student.name, "email": new_student.email}}), 201
```