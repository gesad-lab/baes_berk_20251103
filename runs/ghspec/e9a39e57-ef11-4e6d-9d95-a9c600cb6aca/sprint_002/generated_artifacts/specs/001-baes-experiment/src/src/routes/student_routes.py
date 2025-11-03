```python
from flask import request, jsonify
from src.models import Student
from src.utils import validate_email_format  # Assuming a utility function for email validation

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a name and email."""
    data = request.json
    
    # Validate the input data
    name = data.get('name')
    email = data.get('email')
    
    # Check for missing name
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required"}}), 400
    
    # Check for missing email
    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email is required"}}), 400
    
    # Validate email format
    if not validate_email_format(email):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format"}}), 400

    # Create and save the new student
    student = Student(name=name, email=email)
    try:
        db.session.add(student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": {
                "code": "E004",
                "message": "Email must be unique"
            }
        }), 400

    # Return the created student's details
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    }), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's information by their ID."""
    student = Student.query.get(student_id)

    if not student:
        return jsonify({
            "error": {
                "code": "E005",
                "message": "Student not found"
            }
        }), 404

    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    }), 200
```