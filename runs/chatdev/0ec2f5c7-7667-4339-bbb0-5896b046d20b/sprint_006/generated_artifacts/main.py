'''
Database migration script to add Course table, email field to Student table, and Teacher table.
'''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Teacher
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def upgrade():
    # Create tables if they don't exist
    Base.metadata.create_all(engine)  # This creates all tables including teachers
    with engine.connect() as connection:
        # Check if the students table exists before altering
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='students'"))
        if result.fetchone() is not None:
            # Check if the email column already exists
            result = connection.execute(text("PRAGMA table_info(students)"))
            columns = [row[1] for row in result.fetchall()]
            if 'email' not in columns:
                # Now alter the table to add the email column
                connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT NOT NULL'))  # Ensure this is NOT NULL
                # Update existing records with a default email
                connection.execute(text('UPDATE students SET email = "default@example.com" WHERE email IS NULL'))
        # Check if the courses table exists before altering
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='courses'"))
        if result.fetchone() is not None:
            # Check if the teacher_id column already exists
            result = connection.execute(text("PRAGMA table_info(courses)"))
            columns = [row[1] for row in result.fetchall()]
            if 'teacher_id' not in columns:
                # Now alter the table to add the teacher_id column
                connection.execute(text('ALTER TABLE courses ADD COLUMN teacher_id INTEGER'))  # Add teacher_id column
                # Optionally, set a default value for existing records if needed
                # connection.execute(text('UPDATE courses SET teacher_id = NULL WHERE teacher_id IS NULL'))
if __name__ == "__main__":
    upgrade()