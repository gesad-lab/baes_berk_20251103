```python
from flask import Flask, request, jsonify
from src.models import Student
from src.repositories import student_repository
from src.database import db

def create_app():
    app = Flask(__name__)

    @app.route('/students', methods=['POST'])
    def create_student():
        """Create a new student with name and email."""
        data = request.get_json()

        # Validate input data
        if not data or not data.get('name'):
            return jsonify({'error': {'code': 'E001', 'message': 'Name is required.'}}), 400
        if not data.get('email'):
            return jsonify({'error': {'code': 'E001', 'message': 'Email is required.'}}), 400
        
        # Create the student in the repository
        student = student_repository.create_student(name=data['name'], email=data['email'])
        
        return jsonify({'id': student.id, 'name': student.name, 'email': student.email}), 201

    @app.route('/students/<int:id>', methods=['GET'])
    def get_student(id):
        """Retrieve a student by ID."""
        student = student_repository.get_student_by_id(id)
        
        if not student:
            return jsonify({'error': {'code': 'E002', 'message': 'Student not found.'}}), 404

        return jsonify({'id': student.id, 'name': student.name, 'email': student.email}), 200

    return app
```