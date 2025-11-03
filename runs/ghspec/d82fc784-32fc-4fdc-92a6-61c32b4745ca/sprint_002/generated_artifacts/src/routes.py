```python
import logging
from flask import Blueprint, request, jsonify
from app.models import Student
from app import db

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student record with a name and email."""
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        # Log missing information error
        logger.error("Failed to create student - missing name or email.")
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    new_student = Student(name=data['name'], email=data['email'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        # Log successful creation
        logger.info(f"Created student: {new_student.name} with email: {new_student.email}")
        return jsonify(new_student.to_dict()), 201
    
    except Exception as e:
        # Log exception during creation
        logger.exception("Failed to create student due to an unexpected error.")
        return jsonify({"error": {"code": "E002", "message": "Internal server error."}}), 500


@students_bp.route('/students', methods=['GET'])
def get_students():
    """Retrieve all student records."""
    students = Student.query.all()
    student_list = [student.to_dict() for student in students]
    
    # Log retrieval of students
    logger.info("Retrieved student records.")
    
    return jsonify(student_list), 200


@students_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update an existing student's name and email."""
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        # Log missing information error
        logger.error("Failed to update student - missing name or email.")
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    student = Student.query.get(id)
    if not student:
        logger.warning(f"Student with ID {id} not found for update.")
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

    try:
        student.name = data['name']
        student.email = data['email']
        db.session.commit()
        # Log successful update
        logger.info(f"Updated student ID {id} - New name: {student.name}, New email: {student.email}")
        return jsonify(student.to_dict()), 200

    except Exception as e:
        # Log exception during the update
        logger.exception("Failed to update student due to an unexpected error.")
        return jsonify({"error": {"code": "E002", "message": "Internal server error."}}), 500
```