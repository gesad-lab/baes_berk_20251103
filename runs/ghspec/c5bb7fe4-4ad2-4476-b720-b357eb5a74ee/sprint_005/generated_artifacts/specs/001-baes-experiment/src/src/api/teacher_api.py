```python
from flask import Blueprint, request, jsonify
from src.services.teacher_service import create_teacher, get_teacher, update_teacher
from src.exceptions import InvalidInputError

# Create a Blueprint for teacher-related API operations
teacher_api = Blueprint('teacher_api', __name__)

@teacher_api.route('/teachers', methods=['POST'])
def add_teacher():
    """API endpoint to create a new teacher."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Invalid input: name and email are required.'}}), 400

    try:
        teacher = create_teacher(data['name'], data['email'])
        return jsonify(teacher.to_dict()), 201  # Success response with created teacher details
    except InvalidInputError as e:
        return jsonify({'error': {'code': 'E002', 'message': str(e)}}), 400  # Specific error response for invalid data
    except Exception as e:
        # Log the exception for debugging (not user-facing)
        print(f"Error creating teacher: {str(e)}")
        return jsonify({'error': {'code': 'E003', 'message': 'Unexpected error occurred while creating teacher.'}}), 500

@teacher_api.route('/teachers/<int:teacher_id>', methods=['GET'])
def retrieve_teacher(teacher_id):
    """API endpoint to retrieve details of a specific teacher."""
    try:
        teacher = get_teacher(teacher_id)
        if teacher is None:
            return jsonify({'error': {'code': 'E004', 'message': 'Teacher not found.'}}), 404  # Not found response
        return jsonify(teacher.to_dict()), 200  # Success response with teacher details
    except Exception as e:
        print(f"Error retrieving teacher: {str(e)}")
        return jsonify({'error': {'code': 'E003', 'message': 'Unexpected error occurred while retrieving teacher.'}}), 500

@teacher_api.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher_info(teacher_id):
    """API endpoint to update existing teacher's information."""
    data = request.get_json()
    
    # Validate the input
    if not data:
        return jsonify({'error': {'code': 'E001', 'message': 'Invalid input: data is required for update.'}}), 400
    
    try:
        updated_teacher = update_teacher(teacher_id, data.get('name'), data.get('email'))
        if updated_teacher is None:
            return jsonify({'error': {'code': 'E004', 'message': 'Teacher not found for update.'}}), 404  # Not found response
        return jsonify(updated_teacher.to_dict()), 200  # Success response with updated teacher details
    except InvalidInputError as e:
        return jsonify({'error': {'code': 'E002', 'message': str(e)}}), 400  # Specific error response for invalid data
    except Exception as e:
        print(f"Error updating teacher: {str(e)}")
        return jsonify({'error': {'code': 'E003', 'message': 'Unexpected error occurred while updating teacher.'}}), 500
```