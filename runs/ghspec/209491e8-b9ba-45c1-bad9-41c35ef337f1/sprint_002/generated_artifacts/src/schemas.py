from pydantic import BaseModel, EmailStr

class StudentCreateSchema(BaseModel):
    """Schema for creating a new student."""
    name: str  # Name of the student, required
    email: EmailStr  # Email of the student, required and validated as an email address


class StudentResponseSchema(BaseModel):
    """Schema for responding with student details."""
    id: int  # Automatically generated ID
    name: str  # Name of the student
    email: EmailStr  # Email of the student


class StudentUpdateSchema(BaseModel):
    """Schema for updating existing student information."""
    name: str | None = None  # Name of the student, optional for update
    email: EmailStr | None = None  # Email of the student, optional for update

