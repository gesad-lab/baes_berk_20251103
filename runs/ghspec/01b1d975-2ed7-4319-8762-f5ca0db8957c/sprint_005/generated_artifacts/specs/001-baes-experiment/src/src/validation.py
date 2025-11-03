```python
from flask import request, jsonify
from src.models import db, Teacher
from marshmallow import Schema, fields, ValidationError

class TeacherSchema(Schema):
    name = fields.String(required=True, error_messages={"required": "Name is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required."})

def create_teacher():
    """Create a new Teacher."""
    json_data = request.get_json()

    # Validate incoming JSON data
    try:
        validated_data = TeacherSchema().load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Validation error", "details": err.messages}}), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=validated_data["name"], email=validated_data["email"])

    # Add the teacher to the database
    db.session.add(new_teacher)
    db.session.commit()

    # Respond with the newly created Teacher's ID
    return jsonify({"message": "Teacher created successfully", "teacher_id": new_teacher.id}), 201

def get_teacher(teacher_id):
    """Retrieve Teacher details by ID."""
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404

    # Return Teacher details
    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200
```