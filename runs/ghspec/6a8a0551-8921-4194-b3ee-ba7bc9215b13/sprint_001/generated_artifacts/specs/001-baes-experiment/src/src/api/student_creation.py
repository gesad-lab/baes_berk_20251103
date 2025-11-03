from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Define a schema for validating student data
class StudentSchema(Schema):
    name = fields.String(required=True)

# Create an instance of the schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@app.before_first_request
def create_tables():
    """Create the database tables before the first request."""
    db.create_all()

@app.route('/students/', methods=['POST'])
def create_student():
    """Create a new student."""
    try:
        # Validate and deserialize input data
        student_data = student_schema.load(request.json)
    except ValidationError as err:
        # Return validation errors with a 400 status code
        return jsonify({"error": {"code": "E400", "message": "Invalid input", "details": err.messages}}), 400

    # Create a new Student instance
    new_student = Student(name=student_data['name'])
    
    # Add to the session and commit to the database
    db.session.add(new_student)
    db.session.commit()

    # Return the created student as a response
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

# Additional endpoints would go here (GET, DELETE, etc.)

if __name__ == '__main__':
    app.run(debug=True)