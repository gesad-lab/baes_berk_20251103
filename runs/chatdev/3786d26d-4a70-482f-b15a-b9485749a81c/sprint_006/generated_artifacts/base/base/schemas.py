'''
Defines the Pydantic schemas for request and response validation for students and courses.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int]  # List of course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
class EnrollRequest(BaseModel):
    student_id: int
    course_id: int
class Config:
    orm_mode = True