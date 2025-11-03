```python
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask blueprint for student API
student_api = Blueprint('student_api', __name__)
db = SQLAlchemy()

# Student model definition
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Request validation schema using Marshmallow
class StudentSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name is required."})

student_schema = StudentSchema()

@student_api.route('/students', methods=['POST'])
def create_student():
    """Create a new student entry."""
    json_data = request.get_json()
    
    # Validate the incoming request data
    try:
        validated_data = student_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": err.messages}}), HTTPStatus.BAD_REQUEST

    # Proceed to create the student in the database
    new_student = Student(name=validated_data['name'])
    
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"id": new_student.id, "name": new_student.name}), HTTPStatus.CREATED

@student_api.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student by their ID."""
    student = Student.query.get(student_id)
    
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), HTTPStatus.NOT_FOUND
    
    return jsonify({"id": student.id, "name": student.name}), HTTPStatus.OK
```