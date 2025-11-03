```python
from flask import Blueprint, request, jsonify
from models import Teacher
from app import db

# Define a Blueprint for the teachers API
teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher with name and email.

    Request JSON body should include:
        - name (str): The name of the teacher
        - email (str): The email of the teacher
    Returns:
        JSON response with created teacher details and HTTP status code.
    """
    data = request.get_json()

    if not data or not 'name' in data or not 'email' in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input. 'name' and 'email' are required."}}), 400
    
    new_teacher = Teacher(name=data['name'], email=data['email'])
    db.session.add(new_teacher)
    db.session.commit()
    
    return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201


@teachers_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve the details of a specific teacher by ID.

    Arguments:
        teacher_id (int): The ID of the teacher to retrieve.
        
    Returns:
        JSON response with teacher details or a 404 error if not found.
    """
    teacher = Teacher.query.get(teacher_id)

    if teacher is None:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404
    
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200


@teachers_bp.route('/teachers', methods=['GET'])
def list_teachers():
    """Retrieve a list of all teachers.

    Returns:
        JSON response containing a list of teachers.
    """
    teachers = Teacher.query.all()
    teachers_data = [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
    
    return jsonify(teachers_data), 200
```