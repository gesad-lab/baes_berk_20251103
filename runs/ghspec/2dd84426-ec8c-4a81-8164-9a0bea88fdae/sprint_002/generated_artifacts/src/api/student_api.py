```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from src.services.student_service import create_student, retrieve_all_students

router = APIRouter()

# Pydantic model for creating a student
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Ensure that email is a valid email format

# Pydantic model for the response structure of a student
class StudentResponse(BaseModel):
    name: str
    email: EmailStr

@router.post("/students", response_model=StudentResponse, status_code=201)
async def create_student_endpoint(student: StudentCreate):
    """
    Endpoint to create a new student.
    
    - **student**: The student's details, including name and email.
    
    Returns a response with the details of the created student.
    """
    try:
        # Call the service layer to create a student
        created_student = await create_student(student.name, student.email)
        return created_student
    except Exception as e:
        # Handle potential exceptions during student creation
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/students", response_model=list[StudentResponse])
async def get_all_students():
    """
    Endpoint to retrieve all students.
    
    Returns a list of all students with their names and emails.
    """
    try:
        students = await retrieve_all_students()
        return students
    except Exception as e:
        # Handle potential exceptions during retrieving students
        raise HTTPException(status_code=500, detail=str(e))
```