```python
from flask import Blueprint, request, jsonify, abort
from src.database import db
from src.models import Student
from src.schemas import StudentSchema

students_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    # Validate the incoming request
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description='{"error": {"code": "E001", "message": "Missing required fields: name and email.", "details": {}}}')

    # Extract and validate fields
    name = data.get('name')
    email = data.get('email')

    # Create a new Student instance
    new_student = Student(name=name, email=email)

    # Add the new student to the database
    db.session.add(new_student)
    db.session.commit()

    # Serialize and return the newly created student
    student_schema = StudentSchema()
    return jsonify(student_schema.dump(new_student)), 201
```