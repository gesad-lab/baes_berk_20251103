```python
import json
import logging
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.teacher import Teacher  # Assuming Teacher model is defined in models.teacher
from marshmallow import Schema, fields, ValidationError

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a new Blueprint for teacher routes
teacher_routes = Blueprint('teacher_routes', __name__)

# Define a schema for teacher input validation
class TeacherSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

teacher_schema = TeacherSchema()

@teacher_routes.route('/teachers', methods=['POST'])
def create_teacher():
    """Endpoint to add a new teacher."""
    try:
        # Validate incoming data against the schema
        data = teacher_schema.load(request.json)

        # Create a new Teacher object
        new_teacher = Teacher(name=data['name'], email=data['email'])
        
        # Add the teacher to the database session
        db.session.add(new_teacher)
        db.session.commit()

        logger.info(f"Added new teacher: {new_teacher.name} with email: {new_teacher.email}")

        return jsonify({'id': new_teacher.id, 'name': new_teacher.name, 'email': new_teacher.email}), 201

    except ValidationError as err:
        logger.error(f"Validation error while adding teacher: {err.messages}")
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400
    except Exception as e:
        logger.exception("An error occurred while creating a teacher.")
        return jsonify({"error": {"code": "E002", "message": "Internal server error"}}), 500

@teacher_routes.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Endpoint to retrieve information about a specific teacher."""
    try:
        # Fetch the teacher by ID
        teacher = Teacher.query.get_or_404(teacher_id)
        logger.info(f"Retrieved teacher: {teacher.name} with email: {teacher.email}")

        return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 200

    except Exception as e:
        logger.exception("An error occurred while retrieving teacher information.")
        return jsonify({"error": {"code": "E002", "message": "Internal server error"}}), 500
```