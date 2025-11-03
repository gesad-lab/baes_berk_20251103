from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str  # Required name field for the student
    email: EmailStr  # Required email field for the student, validated as an email format

class StudentResponse(BaseModel):
    """Schema for responding with student details."""
    id: int  # Unique identifier for the student
    name: str  # Name of the student
    email: EmailStr  # Email of the student

class StudentUpdate(BaseModel):
    """Schema for updating a student's email."""
    email: EmailStr  # New email address to update for the student

# Example usage of the schemas in routes could involve creating a student like this:
# @app.post("/students/", response_model=StudentResponse)
# async def create_student(student: StudentCreate):
#     ...  # handle student creation
