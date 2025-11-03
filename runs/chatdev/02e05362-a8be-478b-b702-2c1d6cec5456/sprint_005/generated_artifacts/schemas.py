'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add email field
    courses: list[int] = []  # Add courses field
    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'
class TeacherCreate(BaseModel):  # New TeacherCreate schema
    name: str
    email: str
class TeacherResponse(BaseModel):  # New TeacherResponse schema
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True  # Updated from 'orm_mode' to 'from_attributes'