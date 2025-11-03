```python
# src/services/teacher.py

from flask import jsonify, request, abort
from src.models.teacher import Teacher
from src.db.database import db_session

class TeacherService:
    """Service for managing Teacher entities."""
    
    @staticmethod
    def create_teacher():
        """
        Create a new teacher entry.

        Expects a JSON payload with 'name' and 'email'.

        Returns:
            JSON response with created teacher data or an error message.
        """
        data = request.get_json()

        # Validate the input
        if not data:
            return jsonify({"error": {"code": "E001", "message": "No input data provided."}}), 400
        if 'name' not in data or not data['name']:
            return jsonify({"error": {"code": "E002", "message": "The 'name' field is required."}}), 400
        if 'email' not in data or not data['email']:
            return jsonify({"error": {"code": "E003", "message": "The 'email' field is required."}}), 400
        
        # Create a new Teacher instance
        new_teacher = Teacher(name=data['name'], email=data['email'])
        
        # Save the teacher to the database
        try:
            db_session.add(new_teacher)
            db_session.commit()
            return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
        except Exception as e:
            db_session.rollback()
            return jsonify({"error": {"code": "E004", "message": "Failed to create teacher.", "details": str(e)}}), 500
        
    @staticmethod
    def get_teacher(teacher_id):
        """
        Retrieve a teacher's information by ID.
        
        Args:
            teacher_id: UUID of the teacher to retrieve.
        
        Returns:
            JSON response with teacher data or a 404 error if not found.
        """
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return jsonify({"error": {"code": "E005", "message": "Teacher not found."}}), 404
        
        return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200

    @staticmethod
    def update_teacher(teacher_id):
        """
        Update a teacher's information.

        Expects a JSON payload with fields to update (email and/or name).

        Returns:
            JSON response with updated teacher data or an error message.
        """
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return jsonify({"error": {"code": "E005", "message": "Teacher not found."}}), 404
        
        data = request.get_json()
        if data:
            if 'name' in data:
                teacher.name = data['name']
            if 'email' in data:
                teacher.email = data['email']

            try:
                db_session.commit()
                return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
            except Exception as e:
                db_session.rollback()
                return jsonify({"error": {"code": "E004", "message": "Failed to update teacher.", "details": str(e)}}), 500
        
        return jsonify({"error": {"code": "E006", "message": "No update data provided."}}), 400
```