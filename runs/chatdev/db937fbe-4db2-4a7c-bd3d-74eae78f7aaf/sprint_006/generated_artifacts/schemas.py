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
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Added email field to response schema
    courses: List[int]  # Updated to represent the course IDs associated with the student
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    '''
    name: str
    level: str
    teacher_id: int  # Added teacher_id field to associate a teacher with the course
class CourseResponse(BaseModel):
    '''
    Schema for returning course data.
    '''
    id: int
    name: str
    level: str
    teacher_id: int  # Added teacher_id field to response schema
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