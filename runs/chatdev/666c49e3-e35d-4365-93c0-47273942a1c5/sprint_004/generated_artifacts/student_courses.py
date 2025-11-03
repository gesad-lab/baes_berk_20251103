'''
Defines the association table for the many-to-many relationship between students and courses.
'''
from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)