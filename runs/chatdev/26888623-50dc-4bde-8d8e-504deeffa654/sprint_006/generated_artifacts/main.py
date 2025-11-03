'''
Migration script to add email field to the Student entity and create Course and Teacher tables.
'''
from sqlalchemy import create_engine, text  # Import text for executing raw SQL
from sqlalchemy.orm import sessionmaker
from models import Student, Course, StudentCourse, Teacher
from database import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def migrate_database():
    '''Migrate the database to add email column to the students table, create Teacher table, and add teacher_id to courses.'''
    with engine.connect() as connection:
        # Check if the email column already exists
        result = connection.execute(text("PRAGMA table_info(students);"))
        columns = [row[1] for row in result]
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)  # This will create all tables including the Teacher table
        # Add email column if it doesn't exist
        if 'email' not in columns:
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT;'))
        else:
            print("Email column already exists in the students table.")
        # Check if the teachers table exists
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='teachers';"))
        if not result.fetchone():
            # Create the teachers table if it doesn't exist
            connection.execute(text('CREATE TABLE teachers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL);'))
        # Check if the teacher_id column exists in courses
        result = connection.execute(text("PRAGMA table_info(courses);"))
        columns = [row[1] for row in result]
        if 'teacher_id' not in columns:
            connection.execute(text('ALTER TABLE courses ADD COLUMN teacher_id INTEGER;'))