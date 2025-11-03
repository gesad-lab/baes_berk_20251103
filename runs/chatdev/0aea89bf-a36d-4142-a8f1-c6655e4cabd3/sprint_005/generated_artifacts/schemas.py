'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr
from typing import List
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: EmailStr  # Added email field with validation
    course_ids: List[int] = []  # Added to allow course IDs during student creation
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Added email field to response
    courses: List['CourseResponse']  # Added to return courses in the response
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    '''
    name: str
    level: str
class CourseResponse(BaseModel):
    '''
    Schema for returning course data.
    '''
    id: int
    name: str
    level: str
class TeacherCreate(BaseModel):
    '''
    Schema for creating a new teacher.
    '''
    name: str
    email: EmailStr  # Added email field with validation
class TeacherResponse(BaseModel):
    '''
    Schema for returning teacher data.
    '''
    id: int
    name: str
    email: str