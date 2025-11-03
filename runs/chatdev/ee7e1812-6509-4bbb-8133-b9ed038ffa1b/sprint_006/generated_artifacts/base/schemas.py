'''
Defines the Pydantic models for request validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
    course_ids: List[int] = []  # List of course IDs for enrollment
class CourseCreate(BaseModel):
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: str