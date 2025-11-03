'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field to response model
    courses: List[int]  # List of course IDs associated with the student
class CourseCreate(BaseModel):
    name: str  # Course name is required
    level: str  # Course level is required
    teacher_id: Optional[int]  # Added teacher_id to associate a teacher with the course
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: List[int]  # List of student IDs associated with the course
    teacher_id: Optional[int]  # Added teacher_id to response model
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Email is required and validated
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True