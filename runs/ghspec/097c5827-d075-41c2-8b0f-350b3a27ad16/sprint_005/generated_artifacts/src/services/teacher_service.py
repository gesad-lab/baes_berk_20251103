```python
# src/controllers/teacher_controller.py

from flask import Blueprint, request, jsonify
from src.services.teacher_service import create_teacher, get_teacher
from src.models import Teacher
from werkzeug.exceptions import BadRequest, NotFound

# Define the blueprint for teacher-related routes
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher_endpoint():
    """
    Endpoint to create a new teacher.
    
    Returns:
        JSON response with created teacher details or error message.
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing required fields: 'name' and 'email'.")

    name = data['name']
    email = data['email']

    try:
        # Call service to create teacher
        teacher = create_teacher(name=name, email=email)
        return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 201
    except ValueError as e:
        # Handle validation errors
        raise BadRequest(str(e))

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher_endpoint(teacher_id):
    """
    Endpoint to retrieve a teacher by ID.
    
    Args:
        teacher_id (int): The ID of the teacher to retrieve.
        
    Returns:
        JSON response with teacher details or error message.
    """
    
    try:
        teacher = get_teacher(teacher_id)
        return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 200
    except NotFound:
        raise NotFound(f"Teacher with ID {teacher_id} not found.")
```
