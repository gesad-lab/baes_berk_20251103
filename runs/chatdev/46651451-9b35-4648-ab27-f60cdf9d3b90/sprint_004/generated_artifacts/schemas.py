'''
Defines Pydantic schemas for request and response validation.
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
    courses: List[int]  # Added courses field to represent course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True