```python
from flask import Blueprint, request, jsonify
from src.services.teacher_service import create_teacher, get_teacher_by_id
from src.models import Teacher  # Ensure to import the Teacher model

blueprint = Blueprint('teachers', __name__)

@blueprint.route('/teachers', methods=['POST'])
def add_teacher():
    """
    Create a new teacher in the system.
    Expects a JSON request body containing 'name' and 'email'.

    Returns:
        JSON response indicating success or failure.
    """
    data = request.json
    
    # Validate required fields
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Missing required fields: 'name' and 'email'."
            }
        }), 400
    
    teacher = create_teacher(data['name'], data['email'])
    
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 201

@blueprint.route('/teachers/<int:id>', methods=['GET'])
def get_teacher(id):
    """
    Retrieve details of a teacher by their unique identifier.

    Args:
        id (int): Unique identifier for the teacher.

    Returns:
        JSON response with the teacher's details or an error message.
    """
    teacher = get_teacher_by_id(id)

    if teacher is None:
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Teacher not found."
            }
        }), 404

    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200
```