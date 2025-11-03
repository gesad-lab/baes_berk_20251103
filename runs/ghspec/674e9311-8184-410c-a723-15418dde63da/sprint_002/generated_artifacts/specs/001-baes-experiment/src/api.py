```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # Use your actual database URI
db = SQLAlchemy(app)

# Assuming the Student model is defined somewhere
from models.student import Student

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email.

    Request Body:
    {
        "name": "string",
        "email": "string"
    }
    
    Returns:
    - 201: JSON success message with student information
    - 400: JSON error message for validation issues
    """
    data = request.get_json()

    # Validate input
    if 'email' not in data or not data['email']:
        return jsonify({"error": {"code": "E001", "message": "Email is required."}}), 400

    if not is_valid_email(data['email']):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Create the new student
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student created successfully.", "student": {"name": new_student.name, "email": new_student.email}}), 201

def is_valid_email(email):
    """Validate the email format using a simple regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve the list of all students."""
    students = Student.query.all()
    return jsonify([{"name": student.name, "email": student.email} for student in students])

if __name__ == '__main__':
    app.run(debug=True)
```