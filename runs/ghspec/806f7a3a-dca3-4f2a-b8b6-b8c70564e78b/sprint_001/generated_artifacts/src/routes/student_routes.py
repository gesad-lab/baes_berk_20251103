```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from services.student_service import create_student, get_student_by_id, update_student, delete_student

student_routes = Blueprint('student_routes', __name__)

# Schema for validating student data
class StudentSchema(Schema):
    name = fields.Str(required=True, validate=lambda p: len(p) > 0)

# Instantiate the schema for validation
student_schema = StudentSchema()

@student_routes.route('/students', methods=['POST'])
def add_student():
    """Endpoint to add a new student."""
    json_data = request.get_json()
    try:
        # Validate input data
        data = student_schema.load(json_data)
        # Create student
        student = create_student(data['name'])
        return jsonify({"id": student.id, "name": student.name}), 201
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400
    except Exception as ex:
        return jsonify({"error": {"code": "E002", "message": "Failed to create student", "details": str(ex)}}), 500

@student_routes.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Endpoint to retrieve a student by their ID."""
    student = get_student_by_id(student_id)
    if student:
        return jsonify({"id": student.id, "name": student.name}), 200
    else:
        return jsonify({"error": {"code": "E003", "message": "Student not found"}}), 404

@student_routes.route('/students/<int:student_id>', methods=['PUT', 'PATCH'])
def update_student_info(student_id):
    """Endpoint to update a student's information."""
    json_data = request.get_json()
    try:
        # Validate input data for update
        data = student_schema.load(json_data)
        updated_student = update_student(student_id, data['name'])
        return jsonify({"id": updated_student.id, "name": updated_student.name}), 200
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400
    except Exception as ex:
        return jsonify({"error": {"code": "E002", "message": "Failed to update student", "details": str(ex)}}), 500

@student_routes.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student_info(student_id):
    """Endpoint to delete a student by their ID."""
    try:
        delete_student(student_id)
        return jsonify({"message": "Student deleted successfully"}), 204
    except Exception as ex:
        return jsonify({"error": {"code": "E002", "message": "Failed to delete student", "details": str(ex)}}), 500
```