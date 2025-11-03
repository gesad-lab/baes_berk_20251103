from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
# Load configuration from .env or default settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    """ORM model representing a student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

def initialize_database():
    """Create the database schema if it doesn't exist."""
    with app.app_context():
        db.create_all()  # Create all tables

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a given name."""
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required.'}}), 400

    new_student = Student(name=name)
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id, 'name': new_student.name}), 201
    except IntegrityError as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': {'code': 'E002', 'message': 'Failed to create student.'}}), 500

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's details by their ID."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E003', 'message': 'Student not found.'}}), 404
    return jsonify({'id': student.id, 'name': student.name}), 200

if __name__ == '__main__':
    initialize_database()  # Validate that the database setup is done on startup
    app.run(debug=True)