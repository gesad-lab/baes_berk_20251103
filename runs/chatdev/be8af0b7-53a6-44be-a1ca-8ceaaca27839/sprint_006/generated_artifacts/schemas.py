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
    teacher_id: Optional[int] = None  # Add this line to allow for teacher association
class TeacherCreate(BaseModel):
    name: str
    email: str