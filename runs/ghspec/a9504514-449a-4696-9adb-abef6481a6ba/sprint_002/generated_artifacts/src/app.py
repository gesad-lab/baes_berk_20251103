```python
from flask import Flask, request, jsonify
from src.models import Student, db
import re

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a name and email."""
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create the new student
    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()

    return jsonify({"name": student.name, "email": student.email}), 201

@app.route('/students', methods=['GET'])
def get_all_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    return jsonify([{"name": student.name, "email": student.email} for student in students]), 200

def is_valid_email(email: str) -> bool:
    """Check for a valid email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

if __name__ == '__main__':
    app.run(debug=True)
```