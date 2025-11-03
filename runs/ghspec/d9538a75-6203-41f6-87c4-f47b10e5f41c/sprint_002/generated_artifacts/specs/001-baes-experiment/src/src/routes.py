```python
from flask import Blueprint, request, jsonify
from models import Student, db  # Assuming Student is your model and db is the SQLAlchemy instance
import re

# Create a blueprint for the routes
bp = Blueprint('routes', __name__)

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email: str) -> bool:
    """Helper function to validate email format."""
    return re.match(EMAIL_REGEX, email) is not None

@bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a name and email."""
    data = request.get_json()

    # Check for missing fields
    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create new student record
    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student created successfully.", "student": {
        "id": student.id,
        "name": student.name,
        "email": student.email
    }}), 201

@bp.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()

    # Prepare the list of student records for the response
    student_list = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    
    return jsonify(student_list), 200
```