from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, validator

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Utilizing Pydantic to enforce email validation

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Name is required')
        return v

@router.post("/students", status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student record.

    Args:
        student (StudentCreate): The student details to create a record.

    Returns:
        JSON response with created student details.

    Raises:
        HTTPException: If the name is missing or email is invalid.
    """
    # Here the logic for persisting the student to the database would go

    response = {
        "id": 1,  # This would be the actual created student's ID
        "name": student.name,
        "email": student.email
    }
    return response

# The rest of your API routes and functionality would continue below