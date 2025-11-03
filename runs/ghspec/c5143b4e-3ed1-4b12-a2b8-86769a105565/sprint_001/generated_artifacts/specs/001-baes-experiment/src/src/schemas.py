from pydantic import BaseModel, Field
from typing import List, Optional

class StudentCreate(BaseModel):
    """Schema for creating a new Student."""
    name: str = Field(..., min_length=1, description="The name of the student.")

class StudentRead(BaseModel):
    """Schema for reading a Student's details."""
    id: int
    name: str

    class Config:
        """Pydantic configuration."""
        orm_mode = True  # Allows compatibility with SQLAlchemy models

class StudentList(BaseModel):
    """Schema for returning a list of Students."""
    students: List[StudentRead]  # A list of Student details

    class Config:
        """Pydantic configuration."""
        orm_mode = True  # Allows compatibility with SQLAlchemy models

class ErrorResponse(BaseModel):
    """Schema for structured error responses."""
    error: str
    details: Optional[str] = None