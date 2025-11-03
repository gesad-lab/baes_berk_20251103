```python
from flask import request, jsonify
from src.models.teacher import Teacher
from src.app import db
from flask import Blueprint

# Create a Blueprint for teacher-related routes
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Validate presence of required fields
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required fields."}}), 400

    # Check for unique email
    if Teacher.query.filter_by(email=email).first():
        return jsonify({"error": {"code": "E002", "message": "Email already exists."}}), 409

    # Create new teacher object
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()
    
    return jsonify({
        "message": "Teacher created successfully.",
        "teacher": {
            "id": new_teacher.id,
            "name": new_teacher.name,
            "email": new_teacher.email
        }
    }), 201

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    # Retrieve teacher by ID
    teacher = Teacher.query.get(teacher_id)
    
    if not teacher:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    # Return teacher's details if found
    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200

# Register the blueprint with your app
# Make sure this is done in your app initialization code
# app.register_blueprint(teacher_bp)
```