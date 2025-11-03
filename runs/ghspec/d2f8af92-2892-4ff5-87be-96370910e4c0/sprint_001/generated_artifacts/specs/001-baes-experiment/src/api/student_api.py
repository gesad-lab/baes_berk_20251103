```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """This class represents the student record in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the student model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/api/v1/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    data = request.get_json()
    if not data or 'name' not in data:
        # If the request does not contain a name, return a 400 response
        return jsonify({"error": {"code": "E001", "message": "Invalid request body"}}), 400
    
    new_student = Student(name=data['name'])
    try:
        db.session.add(new_student)
        db.session.commit()
        # Return created student with 201 status code
        return jsonify(new_student.to_dict()), 201
    except IntegrityError:
        # Handle integrity errors (like duplicate entries)
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Student could not be created"}}), 400

@app.route('/api/v1/students', methods=['GET'])
def retrieve_students():
    """Retrieve a list of all student records."""
    try:
        students = Student.query.all()
        return jsonify([student.to_dict() for student in students]), 200
    except Exception as e:
        # Log exception details if necessary and return 500 response
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve student records"}}), 500

@app.route('/api/v1/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student record."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid request body"}}), 400

    student = Student.query.get(student_id)
    if student is None:
        return jsonify({"error": {"code": "E004", "message": "Student not found"}}), 404

    student.name = data['name']
    db.session.commit()
    return jsonify(student.to_dict()), 200

@app.route('/api/v1/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student record."""
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({"error": {"code": "E004", "message": "Student not found"}}), 404

    db.session.delete(student)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```