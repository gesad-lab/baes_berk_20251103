```python
# src/controllers/teacher_controller.py

from flask import Blueprint, request, jsonify
from your_app_name.models import Teacher  # Adjust according to your application structure
from your_app_name import db  # Adjust according to your application structure

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Handle the creation of a new teacher.

    Request body must include:
    - name (str): The name of the teacher
    - email (str): The email of the teacher

    Returns:
    - JSON response with confirmation or error message.
    """
    data = request.get_json()

    # Validate the request data
    if not data or 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    
    if 'email' not in data or not data['email']:
        return jsonify({"error": {"code": "E002", "message": "Email field is required."}}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=data['name'], email=data['email'])
    
    try:
        # Add the new teacher to the database
        db.session.add(new_teacher)
        db.session.commit()
    except Exception as e:
        # Log the error for debugging, don't expose to user
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": {"code": "E003", "message": "An error occurred while saving the teacher."}}), 500

    return jsonify({"success": True, "teacher": {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}}), 201
```