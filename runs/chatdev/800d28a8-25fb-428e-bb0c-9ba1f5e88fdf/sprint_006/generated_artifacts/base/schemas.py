'''
Defines the Pydantic models for the Student, Course, and Teacher entities.
'''
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation