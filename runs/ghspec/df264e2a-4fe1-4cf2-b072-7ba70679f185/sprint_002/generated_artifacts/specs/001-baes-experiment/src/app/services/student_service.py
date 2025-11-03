```python
# app/services/student_service.py

from app.models.student import Student  # Assuming Student model is defined in this module
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

class StudentService:
    """Service for managing student records."""

    @staticmethod
    def create_student(student_data):
        """Create a new student record.

        Args:
            student_data (dict): Dictionary containing student 'name' and 'email'.

        Returns:
            JSON response with student details or error message.
        """
        name = student_data.get("name")
        email = student_data.get("email")

        # Validate input
        if not name:
            return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
        
        if not email:
            return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400

        # Simple regex for email validation; could be enhanced with more detailed checks
        if not StudentService.is_valid_email(email):
            return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

        # Create a new student record
        new_student = Student(name=name, email=email)
        
        try:
            # Assuming db.session is set up for database interaction
            db.session.add(new_student)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": {"code": "E004", "message": "A student with this email already exists."}}), 400

        # Return success response
        return jsonify({"message": "Student created", "student": {"id": new_student.id, "name": new_student.name, "email": new_student.email}}), 201

    @staticmethod
    def retrieve_student(student_id):
        """Retrieve a student record by ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            JSON response with student details or an error message.
        """
        student = Student.query.get(student_id)

        if not student:
            return jsonify({"error": {"code": "E005", "message": "Student not found."}}), 404
        
        return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200

    @staticmethod
    def is_valid_email(email):
        """Validate the format of the email.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Basic email format validation
        return "@" in email and "." in email.split("@")[-1]

```
