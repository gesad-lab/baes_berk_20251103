'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    course_ids: List[int] = []  # Add this line to include course IDs
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List['CourseResponse'] = []  # Ensure this returns course details
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int = None  # Add this line to allow specifying a teacher
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Add this line to return the teacher ID
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