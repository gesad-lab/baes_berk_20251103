'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field
    course_ids: Optional[List[int]] = None  # New field for course IDs
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    courses: List[int]  # List of course IDs
class CourseCreate(BaseModel):
    name: str  # Required field
    level: str  # Required field
class CourseResponse(BaseModel):
    id: int
    name: str  # Required field
    level: str  # Required field
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str