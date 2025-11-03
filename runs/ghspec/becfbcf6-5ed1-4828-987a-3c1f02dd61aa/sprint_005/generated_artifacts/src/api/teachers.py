```python
from flask import Blueprint, request, jsonify
from app import db
from models import Teacher  # Assuming Teacher model is defined in models.py

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new Teacher entity."""
    data = request.get_json()

    # Extracting fields from the request
    name = data.get('name')
    email = data.get('email')

    # Validating required fields
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Missing required fields: name, email."}}), 400
    
    # Check for unique email
    if Teacher.query.filter_by(email=email).first():
        return jsonify({"error": {"code": "E003", "message": "Email must be unique."}}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()
    
    # Return the newly created Teacher's information
    return jsonify({
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }), 201

@teachers_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve a Teacher entity by its ID."""
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404
    
    # Return the Teacher's details
    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200

# Registering the Blueprint with the main app (to be done in the application setup)
# app.register_blueprint(teachers_bp)
```