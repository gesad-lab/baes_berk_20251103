'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str  # Add email field
    course_ids: List[int]  # List of course IDs for the relationship
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response
    course_ids: List[int]  # Include course IDs in response
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    class Config:
        orm_mode = True