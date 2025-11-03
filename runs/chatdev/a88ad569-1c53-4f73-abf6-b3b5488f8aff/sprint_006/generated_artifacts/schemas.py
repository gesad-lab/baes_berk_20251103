'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int] = []  # Add this line to include course IDs
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: Optional[int] = None  # Added teacher_id to associate a teacher
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int] = None  # Added teacher_id in response
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True