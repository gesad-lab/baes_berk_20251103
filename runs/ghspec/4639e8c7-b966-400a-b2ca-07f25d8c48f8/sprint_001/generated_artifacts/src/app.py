from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """Model representing a student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables on application startup."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a name field."""
    data = request.get_json()
    
    # Validate input data
    if 'name' not in data or not isinstance(data['name'], str) or not data['name'].strip():
        return jsonify({'error': {'code': 'E001', 'message': 'Invalid input. Name field is required and must be a non-empty string.'}}), 400
    
    # Create new student instance
    new_student = Student(name=data['name'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
    except IntegrityError:
        return jsonify({'error': {'code': 'E002', 'message': 'Failed to create student, integrity error.'}}), 500

    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)