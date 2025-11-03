```python
# src/controllers/teacher_controller.py

from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from src.models.teacher import Teacher
from src.services.teacher_service import TeacherService
from src.database import get_db  # Assuming a function to get the database session

# Create a Blueprint for the Teacher controller
teacher_blueprint = Blueprint('teacher', __name__)

# Initialize the Teacher Service
teacher_service = TeacherService()

@teacher_blueprint.route('/teachers', methods=['POST'])
def create_teacher():
    """Handle the creation of a new teacher."""
    data = request.json

    try:
        # Validate input data
        teacher = teacher_service.create_teacher(data)
        return jsonify(teacher), 201  # 201 Created
    except ValueError as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400  # Bad Request
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error creating teacher: {e}")
        return jsonify({"error": {"code": "E002", "message": "An error occurred while creating the teacher."}}), 500  # Internal Server Error

@teacher_blueprint.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve a teacher by ID."""
    try:
        teacher = teacher_service.get_teacher(teacher_id)
        if teacher is not None:
            return jsonify(teacher), 200  # 200 OK
        else:
            return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404  # Not Found
    except Exception as e:
        app.logger.error(f"Error retrieving teacher with ID {teacher_id}: {e}")
        return jsonify({"error": {"code": "E002", "message": "An error occurred while retrieving the teacher."}}), 500  # Internal Server Error
```