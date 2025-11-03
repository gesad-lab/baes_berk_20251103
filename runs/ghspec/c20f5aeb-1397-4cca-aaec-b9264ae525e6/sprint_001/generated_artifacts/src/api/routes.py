from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from ..models import db, Student

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the service is running."""
    return jsonify({'status': 'healthy'}), 200

@api.route('/students', methods=['POST'])
def create_student():
    """Create a new Student record."""
    data = request.json
    if 'name' not in data or not data['name']:
        return jsonify({'error': {'code': 'E001', 'message': 'Invalid name: It must be a non-empty string'}}), 400

    try:
        student = Student(name=data['name'])
        db.session.add(student)
        db.session.commit()
        return jsonify({'id': student.id, 'name': student.name}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': {'code': 'E002', 'message': 'Database error occurred', 'details': str(e)}}), 500

@api.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all Student records."""
    try:
        students = Student.query.all()
        return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': {'code': 'E003', 'message': 'Database error occurred', 'details': str(e)}}), 500