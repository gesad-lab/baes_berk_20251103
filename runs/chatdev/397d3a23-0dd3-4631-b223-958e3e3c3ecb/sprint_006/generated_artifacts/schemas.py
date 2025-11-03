'''
Defines the Pydantic models for request and response schemas.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # New email field added
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added teacher_id to associate a teacher with the course
class TeacherCreate(BaseModel):
    name: str
    email: str