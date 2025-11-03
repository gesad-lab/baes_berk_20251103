from flask import Blueprint, jsonify, request
from app.models import Student
from app import db

student_bp = Blueprint('student', __name__)

@student_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a student record by ID, including email."""
    student = Student.query.get(id)
    
    if not student:
        return jsonify(error={'code': 'E002', 'message': 'Student not found'}), 404
    
    return jsonify(id=student.id, name=student.name, email=student.email), 200