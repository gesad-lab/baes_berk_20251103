```python
from flask import Blueprint, jsonify, request
from app import db
from app.models import Teacher  # Ensure Teacher model is imported

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
def get_teachers():
    """
    Retrieve all Teacher entities.

    Returns:
        JSON response containing a list of all teachers.
    """
    try:
        teachers = Teacher.query.all()
        result = [{'id': teacher.id, 'name': teacher.name, 'email': teacher.email} for teacher in teachers]
        return jsonify(result), 200
    except Exception as e:
        # Log the error for debugging (not exposing to the user)
        app.logger.error(f"Failed to retrieve teachers: {str(e)}")
        return jsonify(error={'code': 'E500', 'message': 'Internal server error.'}), 500

# Register the blueprint in the main application
# Assuming this is being done in an "app.py" or similar file
# app.register_blueprint(teacher_bp)
```