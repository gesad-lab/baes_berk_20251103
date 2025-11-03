'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine, Column, String, Integer, text  # Import text for SQL execution
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def create_database():
    '''
    Creates the database and tables if they do not exist.
    '''
    Base.metadata.create_all(bind=engine)
def migrate_database():
    '''
    Migrates the database to add the email field to the Student entity and create the Course table.
    '''
    with engine.connect() as connection:
        # Check if the 'email' column already exists
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            connection.execute(text('ALTER TABLE students ADD COLUMN email VARCHAR'))
        # Create the courses table if it does not exist
        Base.metadata.create_all(bind=engine)  # This will create the courses table if it does not exist
        # Create the association table for student_courses if it does not exist
        connection.execute(text('CREATE TABLE IF NOT EXISTS student_courses (student_id INTEGER, course_id INTEGER, PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(id), FOREIGN KEY (course_id) REFERENCES courses(id))'))
def get_db() -> Session:
    '''
    Dependency that provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()