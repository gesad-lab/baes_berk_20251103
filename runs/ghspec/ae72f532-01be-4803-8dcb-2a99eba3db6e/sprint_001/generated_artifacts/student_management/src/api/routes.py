```python
from flask import Blueprint, request, jsonify
from src.services.student_service import create_student, get_student
from src.models.student import Student

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['POST'])
def add_student():
    """
    Endpoint to create a student record.
    
    Returns:
        JSON response with the created student details or error message.
    """
    try:
        data = request.json
        student_name = data.get('name')
        
        if not student_name:
            return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400
        
        student = create_student(student_name)
        return jsonify(student), 201
    except Exception as e:
        return jsonify({'error': {'code': 'E002', 'message': str(e)}}), 500

@student_routes.route('/students/<int:student_id>', methods=['GET'])
def retrieve_student(student_id):
    """
    Endpoint to retrieve a student record by ID.
    
    Parameters:
        student_id (int): ID of the student to retrieve.
        
    Returns:
        JSON response with student details or error message.
    """
    try:
        student = get_student(student_id)
        if student is None:
            return jsonify({'error': {'code': 'E003', 'message': 'Student not found'}}), 404
        
        return jsonify(student), 200
    except Exception as e:
        return jsonify({'error': {'code': 'E002', 'message': str(e)}}), 500
```