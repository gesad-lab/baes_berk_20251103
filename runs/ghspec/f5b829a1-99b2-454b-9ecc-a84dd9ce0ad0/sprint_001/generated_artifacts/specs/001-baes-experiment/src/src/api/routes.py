from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()

# Error message structure
class ErrorResponse(BaseModel):
    error: dict

# Student model
class Student(BaseModel):
    id: int
    name: str = Field(..., description="The name of the student.")

# In-memory database for demonstration purposes
students_db = {}
student_id_counter = 1

@router.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    global student_id_counter
    
    # Validate the input
    if not student.name:
        error_message = {
            "code": "E001",
            "message": "Name field is required.",
            "details": {}
        }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=ErrorResponse(error=error_message).dict())
    
    # Create student entry
    student.id = student_id_counter
    students_db[student_id_counter] = student
    student_id_counter += 1
    
    return student

@router.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    student = students_db.get(student_id)
    
    if not student:
        error_message = {
            "code": "E002",
            "message": "Student not found.",
            "details": {}
        }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=ErrorResponse(error=error_message).dict())
    
    return student