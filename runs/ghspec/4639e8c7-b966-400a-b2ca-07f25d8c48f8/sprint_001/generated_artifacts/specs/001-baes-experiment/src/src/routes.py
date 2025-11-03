from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    """Model to represent a student."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a name."""
    data = request.get_json()
    if not data or 'name' not in data or not isinstance(data['name'], str):
        return jsonify({"error": {"code": "E001", "message": "Invalid input. Name is required and must be a string."}}), 400
    
    new_student = Student(name=data['name'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"id": new_student.id, "name": new_student.name}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Unable to create student."}}), 500

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)