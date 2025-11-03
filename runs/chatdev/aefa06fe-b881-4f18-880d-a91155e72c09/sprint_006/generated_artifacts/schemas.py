'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response
    course_ids: List[int]  # Include course IDs in response
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add teacher_id field
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Include teacher_id in response
class TeacherCreate(BaseModel):
    name: str
    email: str  # Add email field for Teacher
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response