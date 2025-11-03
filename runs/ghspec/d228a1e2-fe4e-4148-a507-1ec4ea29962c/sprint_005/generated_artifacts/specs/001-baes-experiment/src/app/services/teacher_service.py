```python
# app/services/teacher_service.py

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models import Teacher  # Assuming Teacher model will be defined similar to Course

db = SQLAlchemy()

class TeacherService:
    """Service class for managing teachers."""

    @staticmethod
    def create_teacher(name: str, email: str) -> dict:
        """
        Create a new teacher.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            dict: A response dictionary with the status and created teacher information or error message.
        """
        if not name or not email:
            return {"error": {"code": "E001", "message": "Name and email are required."}}, 400

        if Teacher.query.filter_by(email=email).first():
            return {"error": {"code": "E002", "message": "Email must be unique."}}, 400
        
        new_teacher = Teacher(name=name, email=email)
        db.session.add(new_teacher)
        try:
            db.session.commit()
            return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
        except Exception as e:
            db.session.rollback()
            return {"error": {"code": "E003", "message": "Failed to create teacher. Please try again."}}, 500

    @staticmethod
    def list_teachers() -> list:
        """
        Retrieve a list of teachers.

        Returns:
            list: A list of teachers with their ID, name, and email.
        """
        teachers = Teacher.query.all()
        return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]

    @staticmethod
    def get_teacher_details(teacher_id: int) -> dict:
        """
        Retrieve details of a specific teacher by ID.

        Args:
            teacher_id (int): The ID of the teacher.

        Returns:
            dict: Teacher details or error message if not found.
        """
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            return {"error": {"code": "E004", "message": "Teacher not found."}}, 404

        return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
```