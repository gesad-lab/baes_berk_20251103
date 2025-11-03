'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int]  # Added to include course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int]  # Made optional to handle courses without a teacher
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str