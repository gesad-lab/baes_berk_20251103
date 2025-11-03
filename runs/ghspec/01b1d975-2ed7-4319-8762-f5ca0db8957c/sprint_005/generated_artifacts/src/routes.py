```python
from flask import Blueprint, request, jsonify
from src.models import db, Teacher
from sqlalchemy.exc import IntegrityError

# Initialize the routes blueprint
routes = Blueprint('routes', __name__)

@routes.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new Teacher.
    
    Request Body:
        - name (string, required)
        - email (string, required)
    
    Returns:
        - JSON with Teacher's ID on success (201)
        - Error message on validation failure (400)
    """
    data = request.get_json()

    # Validate input data
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": "Both name and email are required."}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=name, email=email)
    
    try:
        db.session.add(new_teacher)  # Add the new teacher to the session
        db.session.commit()  # Commit the session to persist changes
    except IntegrityError:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": f"Teacher with email '{email}' already exists."}), 400

    return jsonify({"id": new_teacher.id}), 201  # Return newly created Teacher's ID

@routes.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieve details of a Teacher by ID.
    
    Returns:
        - JSON with Teacher's details on success (200)
        - Error message if Teacher does not exist (404)
    """
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": "Teacher not found."}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```