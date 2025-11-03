import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

# Initialize Flask application
app = Flask(__name__)

# Load configuration from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define a schema for serializing Student objects
class StudentSchema(Schema):
    id = fields.Int()
    name = fields.Str()

# Create the SQLite database schema on startup
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a student
@app.route('/students/', methods=['POST'])
def create_student():
    """Create a new student"""
    from flask import request, jsonify
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
        
    student = Student(name=data['name'])
    db.session.add(student)
    db.session.commit()
    
    return jsonify(StudentSchema().dump(student)), 201

# Endpoint to fetch all students
@app.route('/students/', methods=['GET'])
def get_students():
    """Retrieve all students"""
    students = Student.query.all()
    return jsonify(StudentSchema(many=True).dump(students)), 200

# Endpoint to retrieve a specific student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a specific student"""
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    return jsonify(StudentSchema().dump(student)), 200

# Endpoint to delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """Delete a specific student"""
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully."}), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check for the application"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))