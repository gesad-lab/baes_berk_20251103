'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
    course_ids: List[int] = []  # Added course_ids field for enrollment
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    courses: List[CourseResponse]  # Add this line to include courses
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str