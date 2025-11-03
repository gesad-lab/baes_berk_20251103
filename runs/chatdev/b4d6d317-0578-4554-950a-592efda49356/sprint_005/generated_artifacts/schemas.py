'''
Defines the Pydantic models for request validation of the Student, Course, and Teacher entities.
'''
from pydantic import BaseModel
class StudentCreate(BaseModel):
    '''
    Model for creating a new student.
    '''
    name: str
    email: str
class CourseCreate(BaseModel):
    '''
    Model for creating a new course.
    '''
    name: str
    level: str
class TeacherCreate(BaseModel):
    '''
    Model for creating a new teacher.
    '''
    name: str
    email: str