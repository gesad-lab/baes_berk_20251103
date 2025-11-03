from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str  # Required name field
    email: EmailStr  # New required email field with validation
