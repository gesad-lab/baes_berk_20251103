'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    '''Schema for creating a new student.'''
    name: str
    email: str  # Add this line
class StudentResponse(BaseModel):
    '''Schema for returning student data.'''
    id: int
    name: str
    email: str  # Add this line
    courses: List[int] = []  # List of course IDs associated with the student
class CourseCreate(BaseModel):
    '''Schema for creating a new course.'''
    name: str
    level: str
class CourseResponse(BaseModel):
    '''Schema for returning course data.'''
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    '''Schema for creating a new teacher.'''
    name: str
    email: str
class TeacherResponse(BaseModel):
    '''Schema for returning teacher data.'''
    id: int
    name: str
    email: str