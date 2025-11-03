```python
from flask import Flask, request, jsonify
from models import db, Teacher  # Assuming models.py has Teacher defined
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher with name and email."""
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Both name and email are required."}}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=data['name'], email=data['email'])
    
    try:
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({"teacher_id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Email must be unique."}}), 400

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve a teacher's information by ID."""
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    return jsonify({"teacher_id": teacher.id, "name": teacher.name, "email": teacher.email}), 200

@app.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    """Update a teacher's information."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Both name and email are required."}}), 400

    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    teacher.name = data['name']
    teacher.email = data['email']
    db.session.commit()
    
    return jsonify({"teacher_id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```