from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError, DataError
from pydantic import BaseModel, ValidationError

# Importing student service methods
from src.services.student_service import create_student, get_student, update_student, delete_student

# Create a blueprint for the API
api_blueprint = Blueprint('api', __name__)

# Pydantic model for request validation
class StudentModel(BaseModel):
    name: str

@api_blueprint.route('/students', methods=['POST'])
def create_student_route():
    """Create a new student record."""
    try:
        # Validate input data
        student_data = StudentModel(**request.json)
    except ValidationError as e:
        # Return a validation error response
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": e.errors()}}), 400

    try:
        # Call service layer to create the student
        student = create_student(student_data.name)
        return jsonify({"id": student.id, "name": student.name}), 201
    except IntegrityError:
        # Handle case where student already exists
        return jsonify({"error": {"code": "E002", "message": "Student already exists."}}), 409
    except DataError:
        # Handle case where data is not valid for the database
        return jsonify({"error": {"code": "E003", "message": "Invalid data provided."}}), 400
    except Exception as e:
        # Log the error for debugging and return a generic error response
        # Avoid logging sensitive information
        print(f"An error occurred: {str(e)}")  
        return jsonify({"error": {"code": "E004", "message": "Internal server error."}}), 500

@api_blueprint.route('/students/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    """Retrieve a student record by ID."""
    try:
        student = get_student(student_id)
        if student is None:
            return jsonify({"error": {"code": "E005", "message": "Student not found."}}), 404
        return jsonify({"id": student.id, "name": student.name}), 200
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": {"code": "E004", "message": "Internal server error."}}), 500

@api_blueprint.route('/students/<int:student_id>', methods=['PUT'])
def update_student_route(student_id):
    """Update an existing student's name."""
    try:
        # Validate input data
        student_data = StudentModel(**request.json)
    except ValidationError as e:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": e.errors()}}), 400

    try:
        updated_student = update_student(student_id, student_data.name)
        if updated_student is None:
            return jsonify({"error": {"code": "E005", "message": "Student not found."}}), 404
        return jsonify({"id": updated_student.id, "name": updated_student.name}), 200
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Student already exists."}}), 409
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": {"code": "E004", "message": "Internal server error."}}), 500

@api_blueprint.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    """Delete a student record by ID."""
    try:
        success = delete_student(student_id)
        if not success:
            return jsonify({"error": {"code": "E005", "message": "Student not found."}}), 404
        return jsonify({"message": "Student deleted successfully."}), 200
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": {"code": "E004", "message": "Internal server error."}}), 500

