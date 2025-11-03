'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    """
    Schema for creating a new student.
    """
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    """
    Schema for the response of student data.
    """
    id: int
    name: str
    email: str  # Added email field to response
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    """
    Schema for creating a new course.
    """
    name: str
    level: str
class CourseResponse(BaseModel):
    """
    Schema for the response of course data.
    """
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True