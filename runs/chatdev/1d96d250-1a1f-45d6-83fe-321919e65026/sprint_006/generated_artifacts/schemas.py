'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
from typing import List
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: str  # Add email field
    course_ids: List[int] = []  # List of course IDs for enrollment
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Add email field
    courses: List[int]  # List of course IDs the student is enrolled in
    class Config:
        orm_mode = True
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    '''
    name: str
    level: str
    teacher_id: int  # Add this line
class CourseResponse(BaseModel):
    '''
    Schema for returning course data.
    '''
    id: int
    name: str
    level: str
    teacher_id: int  # Add this line
    students: List[int]  # List of student IDs enrolled in the course
    class Config:
        orm_mode = True
class TeacherCreate(BaseModel):
    '''
    Schema for creating a new teacher.
    '''
    name: str
    email: str
class TeacherResponse(BaseModel):
    '''
    Schema for returning teacher data.
    '''
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True