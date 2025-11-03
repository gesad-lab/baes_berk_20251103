'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    course_ids: List[int] = []  # List of course IDs for the relationship
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int]  # List of course IDs the student is enrolled in
    class Config:
        orm_mode = True
# Course schemas
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added to accept teacher ID
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True
# Teacher schemas
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True