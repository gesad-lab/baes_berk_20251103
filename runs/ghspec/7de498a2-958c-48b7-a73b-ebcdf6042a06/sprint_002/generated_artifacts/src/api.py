```python
# File: src/services.py

import re
from fastapi import HTTPException
from typing import Optional

class ServiceClass:
    """Service class for managing student operations, including email handling."""
    
    @staticmethod
    def validate_email(email: str) -> None:
        """Validate the format of the given email address.
        
        Args:
            email (str): The email address to validate.
        
        Raises:
            HTTPException: If the email format is invalid.
        """
        # Regular expression for validating an Email
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        
        if not re.match(email_regex, email):
            # Log detailed error context for debugging if necessary
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "E001", "message": "Invalid email format."}}
            )
    
    def create_student(self, name: str, email: Optional[str] = None) -> dict:
        """Create a new student with a name and email address.
        
        Args:
            name (str): The name of the student.
            email (Optional[str]): The email address of the student.
        
        Returns:
            dict: A dictionary representation of the created student.
        """
        if email:
            self.validate_email(email)
        
        # Logic to save the student to the database goes here
        # Assuming `database` is a reference to your database layer
        student = {"name": name, "email": email}  # Replace with actual database call
        
        return student

    def update_student(self, student_id: int, name: str, email: Optional[str] = None) -> dict:
        """Update an existing student by ID with new name and email address.
        
        Args:
            student_id (int): The ID of the student to update.
            name (str): The new name of the student.
            email (Optional[str]): The new email address of the student.
        
        Returns:
            dict: A dictionary representation of the updated student.
        """
        if email:
            self.validate_email(email)
        
        # Logic to update the student in the database goes here
        # Assuming `database` is a reference to your database layer
        updated_student = {"id": student_id, "name": name, "email": email}  # Replace with actual database call
        
        return updated_student
```