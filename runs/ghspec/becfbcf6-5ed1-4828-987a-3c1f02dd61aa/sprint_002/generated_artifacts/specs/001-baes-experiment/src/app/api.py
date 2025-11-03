```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.student import Student

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save memory

# Initialize the SQLAlchemy object with the Flask application
db = SQLAlchemy(app)

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new Student with a name and email."""
    data = request.get_json()
    
    # Validate input data
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "The name field is required."}}), 400
    if 'email' not in data or not data['email']:
        return jsonify({"error": {"code": "E002", "message": "The email field is required and must be a valid format."}}), 400
    
    # Create the new student
    new_student = Student(name=data['name'], email=data['email'])  # Assuming email field exists in Student model
    db.session.add(new_student)
    db.session.commit()
    
    # Return success response with the created student's details
    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all Students."""
    students = Student.query.all()
    
    # Return a list of students with their details
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200
```