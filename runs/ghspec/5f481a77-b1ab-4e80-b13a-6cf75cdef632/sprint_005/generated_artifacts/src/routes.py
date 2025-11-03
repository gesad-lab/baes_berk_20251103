```python
from flask import request, jsonify
from marshmallow.exceptions import ValidationError
from src.schemas import TeacherSchema  # Assuming TeacherSchema is defined in schemas.py
from src.models import Teacher  # Assuming Teacher model is defined in models.py
from src.db import db  # Assuming db is set up for database operations

teacher_schema = TeacherSchema()

def create_teacher():
    """Endpoint to create a new Teacher."""
    # Parse and validate the incoming JSON data
    try:
        teacher_data = teacher_schema.load(request.json)
    except ValidationError as err:
        # Return validation errors if the input data is invalid
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": err.messages}}), 400

    # Create a new Teacher object
    new_teacher = Teacher(name=teacher_data['name'], email=teacher_data['email'])
    
    # Save the new Teacher to the database
    db.session.add(new_teacher)
    db.session.commit()
    
    return jsonify({"message": "Teacher created successfully", "teacher": teacher_schema.dump(new_teacher)}), 201

def get_teacher(teacher_id):
    """Endpoint to retrieve a Teacher by ID."""
    # Fetch the Teacher from the database using the provided ID
    teacher = Teacher.query.get(teacher_id)
    
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found"}}), 404

    return jsonify({"teacher": teacher_schema.dump(teacher)}), 200
```