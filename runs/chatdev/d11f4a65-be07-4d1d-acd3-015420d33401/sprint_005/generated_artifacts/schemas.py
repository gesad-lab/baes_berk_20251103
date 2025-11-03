'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
    courses: List[int]  # Added courses field to show associated course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: List[int]  # Added students field to show associated student IDs
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True