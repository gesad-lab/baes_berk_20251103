import os
import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """Model for student records."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables on application startup."""
    db.create_all()

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students])

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student record."""
    from flask import request
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created', 'student': {'id': new_student.id, 'name': new_student.name}}), 201

if __name__ == '__main__':
    # Ensure to run 'pip install -r requirements.txt' in the terminal
    os.system('pip install -r requirements.txt')  # Running pip install for dependencies
    app.run(debug=True)