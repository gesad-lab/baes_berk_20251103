from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    """Model for the Student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Student id={self.id} name={self.name}>"


class StudentSchema(Schema):
    """Schema for validating student data."""
    name = fields.String(required=True, validate=lambda s: bool(s.strip()))


@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with the provided name."""
    json_data = request.get_json()
    schema = StudentSchema()

    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name}), 201


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student by their ID."""
    student = Student.query.get(student_id)
    
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    
    return jsonify({"id": student.id, "name": student.name}), 200


@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)