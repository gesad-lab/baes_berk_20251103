```python
from flask import Blueprint, request, jsonify
from models.teacher import Teacher
from database import db
from schemas.teacher_schema import TeacherSchema

teacher_bp = Blueprint('teachers', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new teacher with provided name and email.
    
    Returns:
        JSON response containing the created teacher's details or an error message.
    """
    try:
        # Validate request data
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": {"code": "E001", "message": "Missing required fields: 'name' and 'email'."}}), 400
        
        # Create teacher instance
        teacher_schema = TeacherSchema()
        teacher_data = teacher_schema.load(data)  # Validate and deserialize input data
        new_teacher = Teacher(**teacher_data)

        # Add teacher to the database
        db.session.add(new_teacher)
        db.session.commit()

        # Return the created teacher details
        return jsonify(teacher_schema.dump(new_teacher)), 201

    except Exception as e:
        # Log error for debugging purposes (ensure logging is configured in your application)
        print(f"Error creating teacher: {str(e)}")  # Replace with proper logging
        return jsonify({"error": {"code": "E002", "message": "Internal server error while creating teacher."}}), 500

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieve information about a teacher by their unique identifier.

    Args:
        teacher_id (int): Unique identifier for the teacher.

    Returns:
        JSON response with the teacher's details or an error message.
    """
    try:
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404
        
        teacher_schema = TeacherSchema()
        return jsonify(teacher_schema.dump(teacher)), 200

    except Exception as e:
        # Log error for debugging purposes
        print(f"Error retrieving teacher: {str(e)}")  # Replace with proper logging
        return jsonify({"error": {"code": "E002", "message": "Internal server error while retrieving teacher."}}), 500
```