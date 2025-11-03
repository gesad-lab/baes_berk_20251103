'''
Defines the Pydantic models for the application entities.
'''
from pydantic import BaseModel
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
    courses: Optional[List[int]] = []  # List of course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: str