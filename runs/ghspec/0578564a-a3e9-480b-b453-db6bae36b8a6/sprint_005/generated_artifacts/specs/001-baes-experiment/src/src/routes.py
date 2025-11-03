```python
# src/routes.py
from flask import request, jsonify
import logging
from .models import db, Teacher

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/api/v1/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        error_message = 'Name and email are required'
        logging.error(f"Error creating teacher: {error_message} - Data provided: {data}")
        return jsonify({'error': {'code': 'E001', 'message': error_message}}), 400
    
    new_teacher = Teacher(name=name, email=email)

    try:
        db.session.add(new_teacher)
        db.session.commit()
    except Exception as e:
        logging.error(f"Error saving teacher to database: {str(e)}")
        db.session.rollback()  # Roll back the session on error
        return jsonify({'error': {'code': 'E002', 'message': 'Failed to create teacher'}}), 500

    return jsonify({'message': 'Teacher created successfully', 'teacher_id': new_teacher.id}), 201

@app.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    # Fetch the teacher by ID
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        error_message = 'Teacher not found'
        logging.error(f"Error retrieving teacher: {error_message} - Teacher ID: {teacher_id}")
        return jsonify({'error': {'code': 'E003', 'message': error_message}}), 404

    return jsonify({'name': teacher.name, 'email': teacher.email}), 200
```