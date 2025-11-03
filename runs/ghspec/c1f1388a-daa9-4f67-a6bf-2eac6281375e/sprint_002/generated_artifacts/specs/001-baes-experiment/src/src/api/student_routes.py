```python
from fastapi import APIRouter, HTTPException
from typing import List
from src.models.student import Student  # Importing the Student model
from src.schemas.student import StudentCreate, StudentResponse  # Importing Pydantic schemas for request/response
from src.services.student_service import create_student, get_student, get_all_students  # Service layer functions

router = APIRouter()

@router.post("/students", response_model=StudentResponse)
async def create_new_student(student: StudentCreate):
    """
    Create a new student with the provided name and email.

    Parameters:
    - student (StudentCreate): The details of the student to be created.

    Returns:
    - StudentResponse: The created student details.
    
    Raises:
    - HTTPException: If the student could not be created, with a status code of 400.
    """
    try:
        # Call the service function to create a new student and save to the database
        return await create_student(student)
    except Exception as e:
        # Handle exceptions that may arise during the student creation process
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/students/{student_id}", response_model=StudentResponse)
async def read_student(student_id: int):
    """
    Retrieve a student by their ID.

    Parameters:
    - student_id (int): The ID of the student to retrieve.

    Returns:
    - StudentResponse: The student details, including name and email.

    Raises:
    - HTTPException: If the student with the given ID doesn't exist, with a status code of 404.
    """
    student = await get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Return the student information found
    return student

@router.get("/students", response_model=List[StudentResponse])
async def read_all_students():
    """
    Retrieve all students.

    Returns:
    - List[StudentResponse]: A list of all students with their details including name and email.
    """
    # Call the service function to retrieve all students
    return await get_all_students()
```