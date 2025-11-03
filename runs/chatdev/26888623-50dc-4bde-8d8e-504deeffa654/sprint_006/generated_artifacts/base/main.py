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
    '''Migrate the database to add email column to the students table and create Teacher table.'''
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
if __name__ == "__main__":
    migrate_database()  # Run the migration