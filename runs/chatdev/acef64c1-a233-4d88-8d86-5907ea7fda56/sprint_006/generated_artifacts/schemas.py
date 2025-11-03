'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int]
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add this line
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Add this line
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True