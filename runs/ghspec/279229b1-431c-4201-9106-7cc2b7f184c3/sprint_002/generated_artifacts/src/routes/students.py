```python
from flask import Blueprint, request, jsonify
from your_app_name.models import Student  # Adjust according to your application structure
from your_app_name import db  # Import the database instance
import re

students_bp = Blueprint('students', __name__)

def is_valid_email(email: str) -> bool:
    """Validates the email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@students_bp.route('/students/<int:id>', methods=['PUT'])
def update_student_email(id):
    """API endpoint to update a student's email by ID.
    
    Request body must include:
    {
        "email": "string"
    }
    
    Returns a success message upon successful update, or an error message if validation fails.
    """
    data = request.get_json()

    if 'email' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Email field is required.'}}), 400

    new_email = data['email']

    if not is_valid_email(new_email):
        return jsonify({'error': {'code': 'E002', 'message': 'Invalid email format.'}}), 400

    student = Student.query.get(id)
    if not student:
        return jsonify({'error': {'code': 'E003', 'message': 'Student not found.'}}), 404

    student.email = new_email
    db.session.commit()

    return jsonify({'message': 'Student email updated successfully.'}), 200

# Register the blueprint in your main application file (not shown)
```