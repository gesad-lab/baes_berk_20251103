```python
from flask import request, jsonify
from your_app_name import db  # Adjust according to your application structure
from your_app_name.models import Student  # Adjust according to your application structure
import re  # Regular expressions for email validation

def is_valid_email(email: str) -> bool:
    """Check if the email format is valid."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def update_student_email(student_id: int):
    """Update a student's email based on student ID and request data.

    Parameters:
        student_id (int): The ID of the student to update.

    Returns:
        JSON response with success message or error details.
    """
    # Retrieve student by ID
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E404", "message": "Student not found."}}), 404
    
    # Extract email from request
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"error": {"code": "E400", "message": "Email field is required."}}), 400

    email = data['email']
    
    # Validate email format
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E400", "message": "Invalid email format."}}), 400

    # Update student's email
    student.email = email
    db.session.commit()  # Commit the changes to the database

    return jsonify({"message": "Student email updated successfully."}), 200
```