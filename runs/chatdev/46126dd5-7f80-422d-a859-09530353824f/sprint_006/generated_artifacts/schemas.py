'''
Defines Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
    course_ids: List[int] = []  # List of course IDs for the relationship
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field to response
    courses: List[int]  # List of course IDs associated with the student
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: Optional[int] = None  # Added teacher_id field for relationship
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int]  # Added teacher_id field in response
    students: List[int]  # List of student IDs associated with the course
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True