```python
from flask import Blueprint, jsonify, request
from models import Teacher  # Assuming Teacher model is already defined
from app import db  # Assuming you have db context in app

# Create a new Blueprint for teachers
teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    """Retrieve teacher details by their ID."""
    # Query the database for the teacher with the given ID
    teacher = Teacher.query.get(id)
    
    if teacher is None:
        # Teacher not found, return a 404 error response
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Teacher not found."
            }
        }), 404

    # Teacher found, return details
    return jsonify({
        "teacher": {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }
    }), 200

# Register the Blueprint in the main application
def register_blueprints(app):
    app.register_blueprint(teachers_bp)
```