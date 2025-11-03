'''
Defines the Pydantic models for the Student and Course entities.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str
    level: str