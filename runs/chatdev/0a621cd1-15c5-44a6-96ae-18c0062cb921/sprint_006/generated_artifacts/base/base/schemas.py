'''
Defines the Pydantic models for the Student and Course entities.
'''
from pydantic import BaseModel
from typing import List  # Ensure this line is present
class StudentCreate(BaseModel):
    name: str
    email: str
    course_ids: List[int] = []  # Optional list of course IDs
class CourseCreate(BaseModel):
    name: str
    level: str