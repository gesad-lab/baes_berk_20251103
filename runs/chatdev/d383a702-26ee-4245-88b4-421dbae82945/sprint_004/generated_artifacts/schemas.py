'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str
class Student(StudentCreate):
    id: int
    courses: List[int] = []  # Add this line to include course IDs
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class Course(CourseCreate):
    id: int
    class Config:
        orm_mode = True