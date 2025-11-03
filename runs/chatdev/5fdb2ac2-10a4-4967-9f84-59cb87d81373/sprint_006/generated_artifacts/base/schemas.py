'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str
    course_ids: List[int] = []  # Add this line to accept course IDs
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response model
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
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