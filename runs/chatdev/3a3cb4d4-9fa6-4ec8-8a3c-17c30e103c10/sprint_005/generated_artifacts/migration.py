'''
Migration script to add Course and Teacher tables while preserving Student data.
'''
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.schema import CreateTable
from models import Course, Teacher
from sqlalchemy import inspect
engine = create_engine("sqlite:///./students.db")
metadata = MetaData(bind=engine)
# Check if the tables already exist
inspector = inspect(engine)
if 'courses' not in inspector.get_table_names():
    with engine.connect() as connection:
        connection.execute(CreateTable(Course.__table__))
if 'teachers' not in inspector.get_table_names():
    with engine.connect() as connection:
        connection.execute(CreateTable(Teacher.__table__))
# Create the association table for the many-to-many relationship
student_courses = Table(
    'student_courses',
    metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
# Create the association table
if 'student_courses' not in inspector.get_table_names():
    with engine.connect() as connection:
        connection.execute(CreateTable(student_courses))