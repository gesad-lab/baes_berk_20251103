from flask import request, jsonify
from marshmallow import Schema, fields, ValidationError
from src.models import Student  # Assuming Student is defined in models.py
from src.database import db  # Assuming db is defined for SQLAlchemy

class StudentSchema(Schema):
    """Schema for validating Student input."""
    name = fields.String(required=True, error_messages={"required": "Name is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required.", "invalid": "Invalid email address."})

student_schema = StudentSchema()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new Student record."""
    json_data = request.get_json()

    # Validate incoming data against the schema
    try:
        validated_data = student_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": str(err.messages)}}), 400

    # Create a new Student instance
    new_student = Student(name=validated_data['name'], email=validated_data['email'])
    
    # Add the student to the database
    db.session.add(new_student)
    db.session.commit()

    # Return details of the created student
    return jsonify({
        "id": new_student.id,
        "name": new_student.name,
        "email": new_student.email
    }), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a Student record by ID."""
    student = Student.query.get_or_404(id)  # Automatically returns 404 if not found
    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email
    })

