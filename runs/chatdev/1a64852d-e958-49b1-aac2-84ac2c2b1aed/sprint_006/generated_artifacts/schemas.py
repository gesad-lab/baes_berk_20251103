'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class CourseDetail(BaseModel):
    id: int
    name: str
    level: str
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[CourseDetail]  # Change to return course details instead of IDs
class CourseCreate(BaseModel):
    name: str  # Required field
    level: str  # Required field
    teacher_id: int  # Added field to associate a teacher
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Added field to return associated teacher ID
class TeacherCreate(BaseModel):
    name: str  # Required field
    email: EmailStr  # Required field
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True