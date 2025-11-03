```python
from flask import Flask, request, jsonify, abort
from models.student import Student
from db.database import db

app = Flask(__name__)

class StudentService:
    """Service class to manage student operations."""

    @staticmethod
    def create_student(data):
        """Create a new student record."""
        if not data or 'name' not in data:
            abort(400, description='E001: Student name is required')

        student = Student(name=data['name'])
        db.session.add(student)
        db.session.commit()
        return jsonify(student.to_dict()), 201

    @staticmethod
    def get_student(student_id):
        """Retrieve a student record by ID."""
        student = Student.query.get(student_id)
        if not student:
            abort(404, description='E002: Student not found')
        return jsonify(student.to_dict()), 200

    @staticmethod
    def update_student(student_id, data):
        """Update an existing student record."""
        if not data or 'name' not in data:
            abort(400, description='E001: Student name is required')

        student = Student.query.get(student_id)
        if not student:
            abort(404, description='E002: Student not found')

        student.name = data['name']
        db.session.commit()
        return jsonify(student.to_dict()), 200

    @staticmethod
    def delete_student(student_id):
        """Delete a student record."""
        student = Student.query.get(student_id)
        if not student:
            abort(404, description='E002: Student not found')

        db.session.delete(student)
        db.session.commit()
        return '', 204
```