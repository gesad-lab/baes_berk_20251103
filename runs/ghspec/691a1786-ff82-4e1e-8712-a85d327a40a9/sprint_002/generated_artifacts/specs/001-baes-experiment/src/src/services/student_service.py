```python
# src/services/student_service.py

from typing import Optional
from pydantic import BaseModel, EmailStr, validator

# Define the Student data model for input validation
class Student(BaseModel):
    id: Optional[int]  # Optional ID field for existing records
    name: str          # Name of the student
    email: EmailStr    # Email must be a valid email format

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or v.isspace():
            raise ValueError('Name must not be empty')
        return v

    @validator('email')
    def email_must_be_valid(cls, v):
        # The EmailStr in Pydantic already validates the email format
        return v

# Function to create a new student
def create_student(student_data: Student):
    """
    Creates a new student record based on the provided data.

    Args:
        student_data (Student): The student data containing name and email.

    Returns:
        dict: The created student record details.
    """
    # Insert logic to save student_data to the database
    # This is a placeholder for the actual implementation
    return {"message": "Student created successfully", "student": student_data}

# Function to retrieve a student by ID (placeholder implementation)
def get_student(student_id: int):
    """
    Retrieves a student record by ID.

    Args:
        student_id (int): The unique identifier for the student.

    Returns:
        dict: The student record details.
    """
    # Insert logic to retrieve a student from the database by ID
    return {"message": "Student retrieved successfully", "student_id": student_id}

# Function to update an existing student record
def update_student(student_id: int, student_data: Student):
    """
    Updates an existing student record.

    Args:
        student_id (int): The unique identifier for the student.
        student_data (Student): The updated student data.

    Returns:
        dict: The updated student record details.
    """
    # Insert logic to update the student record in the database
    return {"message": "Student updated successfully", "student": student_data}
```