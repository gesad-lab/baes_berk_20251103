```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for students
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        abort(400, description="Name is required")

    new_student = Student(name=name)
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"id": new_student.id, "name": new_student.name}), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Student already exists")

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student."""
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        abort(400, description="Name is required")

    student = Student.query.get(student_id)
    if student is None:
        abort(404, description="Student not found")

    student.name = name
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name}), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student."""
    student = Student.query.get(student_id)
    if student is None:
        abort(404, description="Student not found")
    
    db.session.delete(student)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```