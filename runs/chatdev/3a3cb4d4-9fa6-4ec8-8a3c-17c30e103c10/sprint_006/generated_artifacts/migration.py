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
# Backup existing data
existing_students = []
existing_courses = []
existing_teachers = []
with engine.connect() as connection:
    if 'students' in inspector.get_table_names():
        existing_students = connection.execute("SELECT * FROM students").fetchall()
    if 'courses' in inspector.get_table_names():
        existing_courses = connection.execute("SELECT * FROM courses").fetchall()
    if 'teachers' in inspector.get_table_names():
        existing_teachers = connection.execute("SELECT * FROM teachers").fetchall()
# Create new tables
if 'courses' not in inspector.get_table_names():
    with engine.connect() as connection:
        connection.execute(CreateTable(Course.__table__))
if 'teachers' not in inspector.get_table_names():
    with engine.connect() as connection:
        connection.execute(CreateTable(Teacher.__table__))
# Restore existing data
with engine.connect() as connection:
    for student in existing_students:
        connection.execute("INSERT INTO students (id, name, email) VALUES (?, ?, ?)", student)
    for course in existing_courses:
        connection.execute("INSERT INTO courses (id, name, level, teacher_id) VALUES (?, ?, ?, ?)", course)
    for teacher in existing_teachers:
        connection.execute("INSERT INTO teachers (id, name, email) VALUES (?, ?, ?)", teacher)