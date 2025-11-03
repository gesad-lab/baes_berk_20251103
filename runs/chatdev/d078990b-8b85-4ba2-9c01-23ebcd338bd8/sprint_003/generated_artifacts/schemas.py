'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    '''
    Schema for student response.
    '''
    id: int
    name: str
    email: str  # Added email field to response
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    '''
    name: str
    level: str
class CourseResponse(BaseModel):
    '''
    Schema for course response.
    '''
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True