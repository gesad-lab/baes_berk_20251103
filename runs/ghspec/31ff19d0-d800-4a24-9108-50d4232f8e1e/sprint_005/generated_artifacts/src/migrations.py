```python
from flask import request, jsonify
from src.models import Teacher  # Assuming a model is created for Teacher
from src import db  # Importing the database instance
import re

def validate_email(email: str) -> bool:
    """Validate the format of an email address."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_teacher_data(name: str, email: str) -> tuple:
    """Validate teacher's name and email data.

    Args:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.

    Returns:
        tuple: A tuple containing a boolean status and an error message (if any).
    """
    if not name:
        return False, "Name is required."
    if not email:
        return False, "Email is required."
    if not validate_email(email):
        return False, "Invalid email format."

    return True, ""

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """API endpoint to create a new teacher."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Validate input data
    is_valid, error_message = validate_teacher_data(name, email)
    if not is_valid:
        return jsonify({"error": {"code": "E001", "message": error_message}}), 400

    # Check for unique email
    if Teacher.query.filter_by(email=email).first():
        return jsonify({"error": {"code": "E002", "message": "Email must be unique."}}), 400

    # Create a new Teacher entity
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }), 201
```