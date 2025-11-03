from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database schema
with app.app_context():
    db.create_all()

# Validator for student creation
class StudentSchema(Schema):
    name = fields.String(required=True)

student_schema = StudentSchema(many=False)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student entity.
    
    Request Body:
    {
        "name": "Student Name"
    }
    
    Responses:
    - 201 Created with student ID on success
    - 400 Bad Request with error message on validation failure
    """
    try:
        # Validate incoming data
        data = student_schema.load(request.json)
        # Create new student instance
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student created", "id": new_student.id}), 201
    except ValidationError as err:
        return jsonify({"error": "Validation error", "messages": err.messages}), 400

@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all students.
    
    Responses:
    - 200 OK with a JSON array of student names
    """
    students = Student.query.all()
    student_list = [{"id": student.id, "name": student.name} for student in students]
    return jsonify(student_list), 200

if __name__ == '__main__':
    app.run(debug=True)