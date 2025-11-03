```python
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from schemas.teacher_schema import TeacherSchema
from models.teacher import Teacher

# Initialize the Blueprint for teacher routes
teacher_bp = Blueprint('teacher', __name__)
db = SQLAlchemy()

@teacher_bp.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher_details(teacher_id):
    """Retrieve details of a specific teacher by their ID."""
    try:
        # Query the Teacher by ID
        teacher = Teacher.query.get_or_404(teacher_id)

        # If found, return the teacher details
        return jsonify({
            'id': teacher.id,
            'name': teacher.name,
            'email': teacher.email
        }), 200
    
    except Exception as e:
        # Log exception for debugging and return a generic error message
        # Avoid logging sensitive details
        app.logger.error(f"Error retrieving teacher: {e}")
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'An error occurred while retrieving teacher details.'
            }
        }), 500
```