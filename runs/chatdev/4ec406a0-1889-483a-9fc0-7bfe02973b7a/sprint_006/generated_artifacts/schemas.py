'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field to response
    courses: List[int] = []  # Include course IDs in the response
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int = None  # Add this line to allow specifying a teacher when creating a course
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int = None  # Allow for None if no teacher is assigned
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True