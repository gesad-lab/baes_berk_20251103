from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Student model definition
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Marshmallow schema for validation and serialization
class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# API Endpoint to get a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Fetch a student by ID."""
    student = Student.query.get(student_id)

    # Handle case where the student does not exist
    if student is None:
        return jsonify({"error": {"code": "E404", "message": "Student not found", "details": {}}}), 404
    
    # Serialize and return the student's data
    student_schema = StudentSchema()
    return jsonify(student_schema.dump(student)), 200

# API endpoint to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    json_data = request.get_json()
    student_schema = StudentSchema()

    try:
        # Validate and deserialize input data
        student_data = student_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E400", "message": "Invalid input", "details": err.messages}}), 400

    # Create new student and save to the database
    student = Student(name=student_data['name'])
    db.session.add(student)
    db.session.commit()

    return jsonify(student_schema.dump(student)), 201

# Initialize database and create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)