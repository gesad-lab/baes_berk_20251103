from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name field is required"}}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"message": "Student created", "id": new_student.id}), 201


@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name field is required"}}), 400

    student.name = data['name']
    db.session.commit()
    
    return jsonify({"message": "Student updated"}), 200


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    db.session.delete(student)
    db.session.commit()
    
    return jsonify({"message": "Student deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)