from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model definition for Student
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Initialize the database and create the tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data or not isinstance(data['name'], str) or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Invalid name format"}}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Rollback session on error
        return jsonify({"error": {"code": "E002", "message": "Could not create student"}}), 500

    return jsonify({"id": new_student.id, "name": new_student.name}), 201

# Route to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

# Route to update an existing student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    if 'name' not in data or not isinstance(data['name'], str) or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Invalid name format"}}), 400

    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E003", "message": "Student not found"}}), 404
    
    student.name = data['name']

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()  # Rollback session on error
        return jsonify({"error": {"code": "E002", "message": "Could not update student"}}), 500

    return jsonify({"id": student.id, "name": student.name}), 200

# Route to delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E003", "message": "Student not found"}}), 404
    
    db.session.delete(student)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)