from pydantic import BaseModel, Field
from typing import List, Optional


class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., gt=0, description="The age of the student must be greater than 0")
    email: str = Field(..., description="The email address of the student")

class StudentResponse(BaseModel):
    """Schema for returning student details in API responses."""
    id: int = Field(..., description="The unique identifier of the student")
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., description="The age of the student")
    email: str = Field(..., description="The email address of the student")

class StudentListResponse(BaseModel):
    """Schema for returning a list of students."""
    students: List[StudentResponse]
    count: int = Field(..., description="The total number of students")