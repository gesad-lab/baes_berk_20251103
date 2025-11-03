```python
from flask import Flask, request, jsonify
from models import Student, db
from sqlalchemy.exc import IntegrityError
import re

app = Flask(__name__)

# Utility function to validate email format
def is_valid_email(email: str) -> bool:
    # Simple regex for basic email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, email) is not None

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    data = request.json

    # Input validation
    name = data.get('name')
    email = data.get('email')

    if not name or not isinstance(name, str):
        return jsonify({"error": {"code": "E001", "message": "Invalid name: must be a non-empty string."}}), 400

    if not email or not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Create new student
    new_student = Student(name=name, email=email)
    try:
        db.session.add(new_student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Email already exists."}}), 400

    return jsonify({"name": new_student.name, "email": new_student.email}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    student_list = [{"name": student.name, "email": student.email} for student in students]
    
    return jsonify(student_list), 200

# Ensure to run your Flask app (app.run()) as part of your main application logic
```