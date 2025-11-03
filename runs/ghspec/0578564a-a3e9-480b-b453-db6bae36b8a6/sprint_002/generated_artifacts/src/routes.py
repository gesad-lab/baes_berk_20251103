from flask import Flask, request, jsonify
from models import Student, db
import re

app = Flask(__name__)

def is_valid_email(email: str) -> bool:
    """Validate email format using a regular expression."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
    
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Create a new student entry
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "message": "Student created successfully.",
        "student": {
            "id": new_student.id,
            "name": new_student.name,
            "email": new_student.email
        }
    }), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    return jsonify([{
        "id": student.id,
        "name": student.name,
        "email": student.email
    } for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)