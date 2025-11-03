from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import re

# Initialize the Blueprint for student routes
student_routes = Blueprint('student_routes', __name__)
db = SQLAlchemy()

# Student model definition (mock-up)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Schema for validating student inputs
class StudentSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)

    @staticmethod
    def validate_email(value):
        # Basic regex for email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError("Invalid email format.")

# Instantiate the schema
student_schema = StudentSchema()

@student_routes.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    try:
        # Validate input
        data = student_schema.load(request.json)
        new_student = Student(name=data['name'], email=data['email'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify(student_schema.dump(new_student)), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@student_routes.route('/students/<int:id>', methods=['GET'])
def retrieve_student(id):
    """Retrieve a student by ID."""
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E001", "message": "Student not found."}}), 404
    return jsonify(student_schema.dump(student)), 200

@student_routes.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update an existing student."""
    try:
        data = student_schema.load(request.json)
        student = Student.query.get(id)
        if student is None:
            return jsonify({"error": {"code": "E001", "message": "Student not found."}}), 404

        student.name = data['name']
        student.email = data['email']
        db.session.commit()
        return jsonify(student_schema.dump(student)), 200
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500