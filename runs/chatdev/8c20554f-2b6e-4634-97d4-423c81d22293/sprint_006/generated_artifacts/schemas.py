'''
Pydantic schemas for request and response validation.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''
    Schema for creating a new student.
    '''
    name: str
    email: str  # Added email field
class StudentResponse(BaseModel):
    '''
    Schema for returning student data.
    '''
    id: int
    name: str
    email: str  # Added email field
    courses: list[int]  # List of course IDs the student is enrolled in
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
    teacher_id: int  # Added teacher_id field in response
    students: list[int]  # List of student IDs enrolled in the course
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