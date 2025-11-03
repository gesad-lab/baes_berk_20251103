'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List, Optional
class CourseBase(BaseModel):
    name: str
    level: str
class CourseCreate(CourseBase):
    pass
class CourseResponse(CourseBase):
    id: int
    class Config:
        orm_mode = True
class StudentBase(BaseModel):
    name: str
    email: str  # Add email field
class StudentCreate(StudentBase):
    courses: List[CourseCreate] = []  # Allow courses to be added
class StudentResponse(StudentBase):
    id: int
    courses: List[CourseResponse] = []  # Include courses in response
    class Config:
        orm_mode = True