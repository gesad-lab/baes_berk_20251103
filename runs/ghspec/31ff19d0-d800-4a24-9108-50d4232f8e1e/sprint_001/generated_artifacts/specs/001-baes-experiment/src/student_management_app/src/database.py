from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create the database schema
with app.app_context():
    db.create_all()

# Create a student endpoint
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    # Validate request
    if 'name' not in data or not data['name']:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400

    # Create a new student
    new_student = Student(name=data['name'])

    # Add to the session and commit
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        'id': new_student.id,
        'name': new_student.name
    }), 201

# Retrieve all students endpoint
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)