```python
# File: src/models/student.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import re

# Initialize the database
db = SQLAlchemy()

# Define a Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False)  # New field added

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates the provided email format."""
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None

# API endpoint to create a student record
@app.route('/students', methods=['POST'])
def create_student():
    """Creates a new student record in the database."""
    data = request.get_json()

    # Validate input data
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    if 'email' not in data or not data['email']:
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400

    if not Student.validate_email(data['email']):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create new student record
    new_student = Student(name=data['name'], email=data['email'])
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student created successfully.", "id": new_student.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E004", "message": "Failed to create student."}}), 400

# API endpoint to get all student records
@app.route('/students', methods=['GET'])
def get_students():
    """Retrieves a list of all student records."""
    students = Student.query.all()
    return jsonify([{"name": student.name, "email": student.email} for student in students]), 200
```