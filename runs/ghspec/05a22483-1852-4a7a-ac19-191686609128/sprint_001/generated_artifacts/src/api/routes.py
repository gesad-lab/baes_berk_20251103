from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus

# Initialize the Blueprint for API routes
api = Blueprint('api', __name__)

# Initialize the database
db = SQLAlchemy()

# Define the Student model
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

# Create a new student record
@api.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    
    # Validate that the 'name' field is provided
    if not data or 'name' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Missing required field: name'}}), HTTPStatus.BAD_REQUEST
    
    # Create a new student instance
    new_student = Student(name=data['name'])
    
    # Add and commit the new student to the database
    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.to_dict()), HTTPStatus.CREATED

# Fetch all student records
@api.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), HTTPStatus.OK

# Fetch a specific student record by ID
@api.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify(student.to_dict()), HTTPStatus.OK

# Update an existing student record
@api.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()

    if 'name' in data:
        student.name = data['name']
    
    db.session.commit()
    return jsonify(student.to_dict()), HTTPStatus.OK

# Delete a specific student record
@api.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return ('', HTTPStatus.NO_CONTENT)  # Respond with no content status
