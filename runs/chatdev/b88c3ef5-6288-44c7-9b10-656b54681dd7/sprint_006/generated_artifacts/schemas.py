'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added to accept teacher_id when creating a course
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Added to include teacher_id in the response
    class Config:
        orm_mode = True
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[CourseResponse] = []  # Add this line to include courses
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True