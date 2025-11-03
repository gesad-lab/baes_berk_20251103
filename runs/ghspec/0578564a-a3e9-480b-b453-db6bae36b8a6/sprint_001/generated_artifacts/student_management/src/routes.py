from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    """Model representing a student."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student to the database and return the student's details."""
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_student = Student(name=data['name'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({'id': new_student.id, 'name': new_student.name, 'age': new_student.age}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students from the database."""
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name, 'age': student.age} for student in students]), 200

if __name__ == '__main__':
    db.create_all()  # Create the database schema
    app.run(debug=True)  # Start the Flask application