from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///students.db")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Model for Student
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Schema for Student
class StudentSchema(Schema):
    name = fields.String(required=True)

# Create the database and table if it doesn't exist
@app.before_first_request
def create_tables():
    db.create_all()

# API route to register a student
@app.route('/register', methods=['POST'])
def register_student():
    # Validate input data
    try:
        student_schema = StudentSchema()
        data = student_schema.load(request.json)

        # Create new Student object
        new_student = Student(name=data['name'])

        # Add and commit to the database
        db.session.add(new_student)
        db.session.commit()

        return jsonify({"message": "Student registered successfully!"}), 201

    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        # log the exception for debugging
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# API route to retrieve registered students
@app.route('/students', methods=['GET'])
def get_students():
    # Query all students
    students = Student.query.all()
    student_schema = StudentSchema(many=True)
    return jsonify(student_schema.dump(students)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)