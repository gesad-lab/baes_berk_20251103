```python
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models.teacher import Teacher
from database import db  # Import the database session

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher_endpoint():
    """Endpoint to create a new teacher."""
    data = request.json

    # Validate the input data
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Missing required fields: name and email."}}), 400

    name = data['name']
    email = data['email']

    # Basic email validation
    if not isinstance(name, str) or not isinstance(email, str):
        return jsonify({"error": {"code": "E002", "message": "Invalid input types."}}), 400

    if not validate_email_format(email):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create a new Teacher instance and add to the database
    try:
        new_teacher = Teacher(name=name, email=email)
        db.session.add(new_teacher)
        db.session.commit()  # Commit changes to the database
        return jsonify({"message": "Teacher created successfully."}), 201
    except IntegrityError:
        db.session.rollback()  # Rollback if there's an integrity error
        return jsonify({"error": {"code": "E004", "message": "Email must be unique."}}), 400
    except Exception as e:
        db.session.rollback()  # Rollback for any other unexpected error
        return jsonify({"error": {"code": "E005", "message": "An unexpected error occurred.", "details": str(e)}}), 500

@teacher_bp.route('/teachers', methods=['GET'])
def get_all_teachers():
    """Endpoint to retrieve a list of all teachers."""
    teachers = Teacher.query.all()
    response = [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
    return jsonify(response), 200

def validate_email_format(email: str) -> bool:
    """Validate the email format using a simple regular expression."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None
```