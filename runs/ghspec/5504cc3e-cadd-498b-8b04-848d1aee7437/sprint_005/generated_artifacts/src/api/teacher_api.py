```python
from flask import Blueprint, request, jsonify
from src.services.teacher_service import create_teacher, get_teachers
from marshmallow import ValidationError

teacher_api = Blueprint('teacher_api', __name__)

@teacher_api.route('/teachers', methods=['POST'])
def add_teacher():
    """Endpoint to create a new teacher.
    
    Expects JSON payload with 'name' and 'email'.
    Returns the created teacher information or error messages.
    """
    try:
        # Attempt to create a teacher using the service function
        teacher_data = request.get_json()
        teacher = create_teacher(teacher_data)
        return jsonify(teacher), 201  # Return created teacher with status 201
    except ValidationError as e:
        # Handle validation errors from marshmallow
        return jsonify({'error': {'code': 'E001', 'message': 'Validation Error', 'details': e.messages}}), 400
    except Exception as e:
        # Log the exception here for debugging purposes (implement logging based on project logging setup)
        return jsonify({'error': {'code': 'E002', 'message': 'Internal Server Error', 'details': str(e)}}), 500

@teacher_api.route('/teachers', methods=['GET'])
def view_teachers():
    """Endpoint to retrieve a list of all teachers.
    
    Returns a list of teachers with their names and emails.
    """
    try:
        teachers = get_teachers()  # Fetch teachers from the service
        return jsonify(teachers), 200  # Return the list of teachers with status 200
    except Exception as e:
        # Log the exception here for debugging (implement logging based on project logging setup)
        return jsonify({'error': {'code': 'E002', 'message': 'Internal Server Error', 'details': str(e)}}), 500
```