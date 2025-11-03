'''
Defines the Pydantic models for request validation of the application entities.
'''
from pydantic import BaseModel
from typing import Optional  # Import Optional from typing
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: Optional[int]  # Change this line to make teacher_id optional
class TeacherCreate(BaseModel):
    name: str
    email: str