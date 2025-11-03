'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
    course_ids: List[int] = []  # Add course_ids field for relationship
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Add email field
    courses: List[int] = []  # Add courses field to show enrolled courses
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True