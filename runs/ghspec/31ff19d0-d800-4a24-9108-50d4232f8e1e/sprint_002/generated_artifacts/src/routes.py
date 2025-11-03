from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # example db URI
db = SQLAlchemy(app)

# Student model for database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Function to validate email format
def is_valid_email(email):
    """Validate the email format."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student with name and email."""
    data = request.get_json()
    
    # Validate input
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and email are required.'}}), 400

    if not is_valid_email(email):
        return jsonify({'error': {'code': 'E002', 'message': 'Invalid email format.'}}), 400

    # Check for unique email
    if Student.query.filter_by(email=email).first():
        return jsonify({'error': {'code': 'E003', 'message': 'Email must be unique.'}}), 400

    # Create new student
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    response = {
        'id': new_student.id,
        'name': new_student.name,
        'email': new_student.email
    }
    return jsonify(response), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    response = [
        {
            'id': student.id,
            'name': student.name,
            'email': student.email
        } for student in students
    ]
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)