from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str  # The name of the student
    email: EmailStr  # The email of the student, validated as an email format

class StudentResponse(BaseModel):
    """Schema for student response."""
    id: int  # Unique identifier for the student
    name: str  # The name of the student
    email: str  # The email of the student

class StudentUpdateEmail(BaseModel):
    """Schema for updating a student's email."""
    email: EmailStr  # New email for the student, validated as an email format