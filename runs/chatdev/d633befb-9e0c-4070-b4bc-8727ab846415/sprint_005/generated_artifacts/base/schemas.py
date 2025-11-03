'''
Defines Pydantic schemas for request and response validation.
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
    courses: List[int]  # List of course IDs the student is enrolled in
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: List[int]  # List of student IDs enrolled in the course
    class Config:
        orm_mode = True