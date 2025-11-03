'''
Defines the Pydantic models for request validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # New email field added
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add this line
class TeacherCreate(BaseModel):
    name: str
    email: str