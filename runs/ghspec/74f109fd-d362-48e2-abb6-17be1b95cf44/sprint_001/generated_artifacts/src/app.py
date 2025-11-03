from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    """Database model for Student."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class StudentSchema(Schema):
    """Schema for validating student data."""
    name = fields.Str(required=True)

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student.

    Request body should contain a JSON object with the 'name' field.
    Returns the created student object in JSON format.
    """
    json_data = request.get_json()
    schema = StudentSchema()

    try:
        # Validate the incoming data using marshmallow
        data = schema.load(json_data)
    except ValidationError as e:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data.", "details": e.messages}}), 400

    # Create a new student and add to the database
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student by ID.

    Returns the student's ID and name, or an error message if not found.
    """
    student = Student.query.get(student_id)
    
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    
    return jsonify({"id": student.id, "name": student.name}), 200

if __name__ == '__main__':
    app.run(debug=True)