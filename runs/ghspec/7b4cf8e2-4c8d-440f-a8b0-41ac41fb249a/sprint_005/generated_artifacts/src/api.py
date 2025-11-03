```python
from flask import Flask, jsonify, request, abort
from models import db, Teacher
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher."""
    data = request.get_json()
    
    # Validate input data
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    # Create the teacher instance
    new_teacher = Teacher(name=name, email=email)

    try:
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({"message": "Teacher created successfully.", "teacher_id": new_teacher.id}), 201
    except IntegrityError:
        db.session.rollback()  # Roll back the session in case of error
        return jsonify({"error": {"code": "E002", "message": "Email must be unique."}}), 400

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve the details of a specific teacher."""
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404
    
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200

@app.route('/teachers', methods=['GET'])
def list_teachers():
    """Retrieve a list of all teachers."""
    teachers = Teacher.query.all()
    result = [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
    return jsonify(result), 200
```