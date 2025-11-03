from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define the Student model
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

# Create a new blueprint for student routes
student_routes = Blueprint('student_routes', __name__)

def create_error_response(error_code: str, message: str):
    """Helper function to create structured error responses."""
    return jsonify({"error": {"code": error_code, "message": message}}), 400

@student_routes.route('/students', methods=['POST'])
def create_student():
    """Create a new student with the provided name."""
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or not data['name']:
        return create_error_response('E001', 'The name field is required.')

    new_student = Student(name=data['name'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"id": new_student.id, "name": new_student.name}), 201
    except IntegrityError:
        db.session.rollback()
        return create_error_response('E002', 'An error occurred while creating the student.')

@student_routes.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve information about a specific student by ID."""
    student = Student.query.get(student_id)
    
    if student is None:
        return create_error_response('E003', 'Student not found.')
        
    return jsonify({"id": student.id, "name": student.name}), 200
