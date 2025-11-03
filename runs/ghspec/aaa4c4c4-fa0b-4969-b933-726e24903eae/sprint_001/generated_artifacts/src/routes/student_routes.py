```python
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from marshmallow import Schema, fields, ValidationError
from models.student import Student
from database.db import session

student_routes = Blueprint('student_routes', __name__)

class StudentSchema(Schema):
    name = fields.Str(required=True)

student_schema = StudentSchema()

@student_routes.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    try:
        # Validate and deserialize input data
        student_data = student_schema.load(request.json)
        
        # Create a new Student instance
        new_student = Student(name=student_data["name"])
        
        # Add the new student to the session and commit to the database
        session.add(new_student)
        session.commit()
        
        return jsonify({
            "message": "Student created",
            "id": new_student.id,
            "name": new_student.name
        }), 201

    except ValidationError as err:
        # Return validation errors as a 400 Bad Request
        return jsonify({"error": {"code": "E400", "message": "Validation error", "details": err.messages}}), 400

    except IntegrityError:
        session.rollback()  # Rollback on integrity error
        return jsonify({"error": {"code": "E409", "message": "Student already exists"}}), 409

    except SQLAlchemyError as e:
        session.rollback()  # Rollback on any SQLAlchemy error
        return jsonify({"error": {"code": "E500", "message": "Database operation failed", "details": str(e)}}), 500

@student_routes.route('/students', methods=['GET'])
def get_all_students():
    """Retrieve all students."""
    try:
        students = session.query(Student).all()
        result = [{"id": student.id, "name": student.name} for student in students]
        
        return jsonify(result), 200

    except SQLAlchemyError as e:
        return jsonify({"error": {"code": "E500", "message": "Database operation failed", "details": str(e)}}), 500

@student_routes.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    """Retrieve a student by ID."""
    try:
        student = session.query(Student).get(student_id)
        if student is None:
            return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404
        
        return jsonify({"id": student.id, "name": student.name}), 200

    except SQLAlchemyError as e:
        return jsonify({"error": {"code": "E500", "message": "Database operation failed", "details": str(e)}}), 500
```