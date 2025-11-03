from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Route to create a student
@app.route('/students', methods=['POST'])
def create_student():
    """Creates a new student entry."""
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400

    student_name = data['name']
    new_student = Student(name=student_name)
    
    db.session.add(new_student)
    db.session.commit()

    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

# Route to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    """Retrieves a list of all students."""
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

# Create the database and tables
@app.before_first_request
def create_tables():
    """Creates database tables on the first request."""
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)