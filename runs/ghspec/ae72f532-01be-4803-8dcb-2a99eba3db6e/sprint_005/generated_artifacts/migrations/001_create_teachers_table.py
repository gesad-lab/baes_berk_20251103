```python
from flask import Blueprint, request, jsonify
from src.models.teacher import Teacher
from src.services.teacher_service import TeacherService

# Create a new Blueprint for the Teacher API
teacher_bp = Blueprint('teachers', __name__)

@teacher_bp.route('/api/v1/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new teacher.
    Request Body: { "name": "string", "subject": "string" }
    Response: { "id": "int", "name": "string", "subject": "string" }
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'subject' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input, 'name' and 'subject' are required"}}), 400
    
    # Call the service to create a new teacher
    teacher_service = TeacherService()
    try:
        teacher = teacher_service.create_teacher(data['name'], data['subject'])
        return jsonify(teacher), 201
    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500

@teacher_bp.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieve a teacher by their ID.
    Response: { "id": "int", "name": "string", "subject": "string" }
    """
    teacher_service = TeacherService()
    try:
        teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not teacher:
            return jsonify({"error": {"code": "E003", "message": "Teacher not found"}}), 404
        return jsonify(teacher), 200
    except Exception as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500
```