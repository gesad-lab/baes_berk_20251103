'''
Defines the Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str
    course_ids: List[int] = []  # List of course IDs for the relationship
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[int]  # List of course IDs associated with the student
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    name: str
    level: str
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    students: List[int]  # List of student IDs associated with the course
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True