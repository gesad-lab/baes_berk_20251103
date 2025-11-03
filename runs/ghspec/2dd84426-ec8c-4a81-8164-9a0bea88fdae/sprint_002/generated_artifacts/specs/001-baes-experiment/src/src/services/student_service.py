```python
# src/services/student_service.py

from typing import List, Dict, Any
from fastapi import HTTPException
from src.models.student import Student  # Ensure we are importing the Student model
from src.database import get_student_db  # Importing the database functionality
from src.validation.student_validation import validate_student  # Importing validation function

def create_student(student_data: Dict[str, Any]) -> Student:
    """
    Create a new student with the provided data.

    Args:
        student_data (Dict[str, Any]): A dictionary containing student attributes,
                                        specifically 'name' and 'email'.

    Returns:
        Student: The created Student object.

    Raises:
        HTTPException: If the email is missing or if validation fails.
    """
    # Validate student data to ensure it meets the requirements
    name = student_data.get("name")
    email = student_data.get("email")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email is required.")

    # Perform validation checks (this function is assumed to validate both name and email)
    validate_student(name, email)

    # Create a new student instance
    try:
        student = Student(name=name, email=email)
        # Assuming we have a method to save a student in the database
        student_db = get_student_db()  # Retrieves the database session
        student_db.add(student)  # Add student to the session
        student_db.commit()  # Commit the session to the database
        student_db.refresh(student)  # Refresh instance with new information to obtain ID
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the student: {str(e)}")

    return student

def get_all_students() -> List[Student]:
    """
    Retrieve all students from the database.

    Returns:
        List[Student]: A list of all students.
    """
    student_db = get_student_db()  # Retrieves the database session
    return student_db.query(Student).all()  # Return all student records
```