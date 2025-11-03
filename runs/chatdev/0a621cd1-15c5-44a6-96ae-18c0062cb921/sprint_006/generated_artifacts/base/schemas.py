'''
Defines the Pydantic models for the Student, Course, and Teacher entities.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    name: str
    email: str
    course_ids: List[int] = []  # Optional list of course IDs
class CourseCreate(BaseModel):
    name: str
    level: str
class TeacherCreate(BaseModel):
    name: str
    email: str