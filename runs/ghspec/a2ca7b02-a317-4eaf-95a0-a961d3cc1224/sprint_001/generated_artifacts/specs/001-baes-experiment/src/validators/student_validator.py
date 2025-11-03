```python
from pydantic import BaseModel, Field, ValidationError
from typing import List
from fastapi import HTTPException

class StudentCreate(BaseModel):
    """Pydantic model for creating a new student."""
    name: str = Field(..., description="The name of the student, required field")

def validate_student_input(student_data: dict) -> StudentCreate:
    """
    Validate input data for creating a new student.

    Args:
        student_data (dict): The data to validate.

    Returns:
        StudentCreate: A validated StudentCreate model instance.

    Raises:
        HTTPException: If validation fails, raises a 400 Bad Request error.
    """
    try:
        student = StudentCreate(**student_data)
        return student
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_all_students() -> List[str]:
    """
    Stub function to get all students.
    In a real application this would interact with the database.

    Returns:
        List[str]: A list of student names.
    """
    # Placeholder for actual student retrieval - to be implemented in service layer
    return []

def add_student(student_data: dict) -> str:
    """
    Function to add a new student after validating the input.

    Args:
        student_data (dict): The data of the student to add.

    Returns:
        str: A success message indicating the student has been added.

    Raises:
        HTTPException: If validation fails, raises a 400 Bad Request error.
    """
    validated_student = validate_student_input(student_data)
    # Here, add call to service layer to actually save the student
    return f"Student '{validated_student.name}' added successfully."
```