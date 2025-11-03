```python
from flask import Blueprint, request, jsonify
from src.models.teacher_model import Teacher
from src.services.teacher_service import create_teacher, get_teacher_by_id

# Create a blueprint for teacher routes
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def add_teacher():
    """Create a Teacher entity.
    
    Request Body:
        - name (string, required)
        - email (string, required, must be in valid format)

    Returns:
        - 201 Created with a message confirming the teacher creation.
        - 400 Bad Request if name or email is missing or invalid.
    """
    data = request.get_json()
    
    # Validate input
    if 'name' not in data or not data['name'].strip():
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required.'}}), 400
    if 'email' not in data or not data['email'].strip():
        return jsonify({'error': {'code': 'E002', 'message': 'Email is required.'}}), 400
    
    # Attempt to create a teacher
    teacher, error = create_teacher(data['name'], data['email'])
    if error:
        return jsonify({'error': {'code': 'E003', 'message': str(error)}}), 400
    
    return jsonify({'message': 'Teacher created successfully.'}), 201

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve a Teacher entity by ID.

    Returns:
        - 200 OK with teacher details (name and email) in JSON format.
        - 404 Not Found if the teacher does not exist.
    """
    teacher = get_teacher_by_id(teacher_id)
    if not teacher:
        return jsonify({'error': {'code': 'E004', 'message': 'Teacher not found.'}}), 404
    
    return jsonify({'name': teacher.name, 'email': teacher.email}), 200

def register_teacher_routes(app):
    """Register teacher routes with the Flask app."""
    app.register_blueprint(teacher_bp)

# Call this function during the app initialization to register routes
```