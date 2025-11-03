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
    teacher_id: int = None  # Add teacher_id field for relationship
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int = None  # Add this line to include teacher information
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
class Config:
    orm_mode = True