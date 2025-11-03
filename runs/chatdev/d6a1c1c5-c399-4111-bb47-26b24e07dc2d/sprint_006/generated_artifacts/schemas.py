'''
Pydantic models for data validation and serialization.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str  # Required field
    level: str  # Required field
    teacher_id: int  # Added teacher_id field to associate with Teacher
class TeacherCreate(BaseModel):
    name: str
    email: str
class Teacher(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True