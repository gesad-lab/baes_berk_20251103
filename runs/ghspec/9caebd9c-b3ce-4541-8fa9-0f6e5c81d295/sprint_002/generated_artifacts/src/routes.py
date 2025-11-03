```python
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from api.validators import validate_student_name, validate_student_email

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model with an email field
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student."""
    data = request.get_json()
    
    # Validate input data
    try:
        validate_student_name(data['name'])
        validate_student_email(data['email'])  # Validate email
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400
    
    new_student = Student(name=data['name'], email=data['email'])
    
    # Save the new student to database
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({'message': 'Student created', 'id': new_student.id}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's details by ID."""
    student = Student.query.get(student_id)
    
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    
    return jsonify({'name': student.name, 'email': student.email}), 200
```