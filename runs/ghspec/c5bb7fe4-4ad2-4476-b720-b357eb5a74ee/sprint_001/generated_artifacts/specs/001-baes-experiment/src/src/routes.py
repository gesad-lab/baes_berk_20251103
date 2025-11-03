from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """Represents a student in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables on the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'E001: Name is required.'}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'E002: Student name conflicts.'}), 409

    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update an existing student's name."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'E001: Name is required.'}), 400

    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'E003: Student not found.'}), 404

    student.name = data['name']
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name}), 200

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """Delete a student."""
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'E003: Student not found.'}), 404

    db.session.delete(student)
    db.session.commit()
    return '', 204

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to monitor the application."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)