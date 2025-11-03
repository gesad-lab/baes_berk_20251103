'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''Schema for creating a new student.'''
    name: str
    email: str  # Add this line
class StudentResponse(BaseModel):
    '''Schema for returning student data.'''
    id: int
    name: str
    email: str  # Add this line
class CourseCreate(BaseModel):
    '''Schema for creating a new course.'''
    name: str
    level: str
class CourseResponse(BaseModel):
    '''Schema for returning course data.'''
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True