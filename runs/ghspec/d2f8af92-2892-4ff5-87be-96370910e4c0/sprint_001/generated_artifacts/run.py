```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set up the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

# Create the database schema
def create_db():
    with app.app_context():
        db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'E001: Name field is required'}), 400
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

@app.route('/students', methods=['GET'])
def read_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'E001: Name field is required'}), 400
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'E002: Student not found'}), 404
    student.name = data['name']
    db.session.commit()
    return jsonify(student.to_dict()), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'E002: Student not found'}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'}), 204

# Ensure the database is created upon startup
if __name__ == '__main__':
    create_db()  # Create database and tables
    app.run(debug=True)
```