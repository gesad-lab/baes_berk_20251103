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
class TeacherCreate(BaseModel):
    name: str
    email: str