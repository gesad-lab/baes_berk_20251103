from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    """Schema for creating a student."""
    name: str  # Required name field
    email: EmailStr  # Required email field, must be a valid email format


class StudentResponse(BaseModel):
    """Schema for returning a student response."""
    id: int  # Student ID provided by the database
    name: str  # Name of the student
    email: EmailStr  # Email of the student


class StudentListResponse(BaseModel):
    """Schema for returning a list of students."""
    students: list[StudentResponse]  # List of students with response model
