'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List, Optional
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    courses: List[str]
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[str]
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: Optional[int]  # Added teacher_id field
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int]  # Added teacher_id field
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True