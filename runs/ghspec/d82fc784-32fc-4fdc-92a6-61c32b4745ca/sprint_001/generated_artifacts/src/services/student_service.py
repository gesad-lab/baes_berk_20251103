```python
import logging
from typing import List, Dict, Any
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from models import Student  # Assuming a Student model exists in models module
from db import db_session  # Assuming a db_session is set up for database interaction

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StudentService:
    """Service layer for managing Student entities."""
    
    @staticmethod
    def create_student(data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new student record.
        
        Args:
            data (Dict[str, Any]): The student data.

        Returns:
            Dict[str, Any]: The created student record.
        
        Raises:
            ValueError: Raised if input data is invalid.
            Exception: For unexpected errors during database operations.
        """
        # Validate input data
        StudentService.validate_student_data(data)

        new_student = Student(**data)
        try:
            db_session.add(new_student)
            db_session.commit()
            logger.info("Created new student record: %s", new_student)
            return jsonify({"message": "Student created successfully", "student": new_student.to_dict()}), 201
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.error("Database error occurred while creating student: %s", str(e))
            return jsonify({"error": {"code": "E500", "message": "Database error during student creation."}}), 500
        except Exception as e:
            logger.error("Unexpected error occurred: %s", str(e))
            return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred."}}), 500

    @staticmethod
    def validate_student_data(data: Dict[str, Any]):
        """Validate input data for creating/updating a student.
        
        Args:
            data (Dict[str, Any]): The student data to validate.

        Raises:
            ValueError: If validation fails with specific error messages.
        """
        required_fields = ["name", "age", "email"]
        
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Additional specific validations can be added here
        if not isinstance(data["age"], int) or data["age"] < 0:
            raise ValueError("Invalid age provided: must be a non-negative integer.")
        
        if "@" not in data["email"]:
            raise ValueError("Invalid email format provided.")

    @staticmethod
    def get_students() -> List[Dict[str, Any]]:
        """Retrieve all student records.
        
        Returns:
            List[Dict[str, Any]]: A list of all students.
        """
        try:
            students = Student.query.all()
            logger.info("Retrieved %d student records", len(students))
            return [student.to_dict() for student in students]
        except SQLAlchemyError as e:
            logger.error("Database error occurred: %s", str(e))
            raise Exception("Database error occurred while retrieving students.")
```
