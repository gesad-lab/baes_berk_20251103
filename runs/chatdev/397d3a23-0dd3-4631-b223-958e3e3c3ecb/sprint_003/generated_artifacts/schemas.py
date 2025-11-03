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