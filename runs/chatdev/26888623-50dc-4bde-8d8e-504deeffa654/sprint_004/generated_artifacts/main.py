'''
Migration script to add email field to the Student entity and create Course table.
'''
from sqlalchemy import create_engine, text  # Import text for executing raw SQL
from sqlalchemy.orm import sessionmaker
from models import Student, Course, StudentCourse
from database import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def add_email_column():
    '''Add email column to the students table if it doesn't exist.'''
    with engine.connect() as connection:
        # Check if the email column already exists
        result = connection.execute(text("PRAGMA table_info(students);"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT;'))
        else:
            print("Email column already exists in the students table.")
def create_association_table():
    '''Create the association table for student-course relationships.'''
    Base.metadata.create_all(bind=engine)  # Create the tables first
if __name__ == "__main__":
    create_association_table()  # Create tables including the association table
    add_email_column()  # Then run the migration to add the email column