from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Student schema for validation
class StudentSchema(Schema):
    name = fields.String(required=True)

# Create the database and the tables
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoints
@app.route('/students', methods=['POST'])
def create_student():
    json_data = request.json
    # Validate and deserialize input
    try:
        valid_data = StudentSchema().load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Name is required and must be a string.", "details": err.messages}}), 400
    
    student = Student(name=valid_data['name'])
    db.session.add(student)
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    return jsonify({"id": student.id, "name": student.name})

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    json_data = request.json
    # Validate and deserialize input
    try:
        valid_data = StudentSchema().load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Name is required and must be a string.", "details": err.messages}}), 400
    
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    
    student.name = valid_data['name']
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name})

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted."}), 204

if __name__ == '__main__':
    app.run(debug=True)