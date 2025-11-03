'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
from typing import List
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: EmailStr  # Added email field with validation
    course_ids: List[int] = []  # List of course IDs for enrollment
class StudentResponse(BaseModel):
    '''
    Schema for student response.
    '''
    id: int
    name: str
    email: str  # Added email field to response
    courses: List[int] = []  # List of course IDs the student is enrolled in
class CourseCreate(BaseModel):
    '''
    Schema for creating a new course.
    '''
    name: str
    level: str
    teacher_id: int  # Added this line
class CourseResponse(BaseModel):
    '''
    Schema for course response.
    '''
    id: int
    name: str
    level: str
    teacher_id: int  # Added this line
    students: List[int] = []  # List of student IDs enrolled in the course
class TeacherCreate(BaseModel):
    '''
    Schema for creating a new teacher.
    '''
    name: str
    email: EmailStr
class TeacherResponse(BaseModel):
    '''
    Schema for teacher response.
    '''
    id: int
    name: str
    email: str