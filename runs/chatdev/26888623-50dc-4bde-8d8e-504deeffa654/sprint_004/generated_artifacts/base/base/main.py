'''
Migration script to add email field to the Student entity.
'''
from sqlalchemy import create_engine, text  # Import text for executing raw SQL
from sqlalchemy.orm import sessionmaker
from models import Student
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
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # Create tables if they don't exist
    add_email_column()  # Run the migration to add the email column