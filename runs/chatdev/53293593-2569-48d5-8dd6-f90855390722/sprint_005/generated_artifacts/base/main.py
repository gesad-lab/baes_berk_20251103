'''
Handles database migrations to add the email field to the Student entity and create the Course table.
'''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import MetaData
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
# Create a new migration
def migrate():
    metadata = MetaData()
    metadata.reflect(bind=engine)  # Reflect the current database schema
    # Step 1: Create the Course table if it doesn't exist
    if 'courses' not in metadata.tables:
        with engine.connect() as connection:
            connection.execute(text('CREATE TABLE courses (id INTEGER PRIMARY KEY, name TEXT NOT NULL, level TEXT NOT NULL)'))  # Create courses table
    # Step 2: Create a temporary table for student_courses
    if 'student_courses' in metadata.tables:
        with engine.connect() as connection:
            connection.execute(text('CREATE TABLE student_courses_temp (student_id INTEGER, course_id INTEGER, PRIMARY KEY (student_id, course_id))'))  # Create temp table
            connection.execute(text('INSERT INTO student_courses_temp (student_id, course_id) SELECT student_id, course_id FROM student_courses'))  # Copy existing relationships
    # Migrate Student table
    if 'students' in metadata.tables:
        with engine.connect() as connection:
            connection.execute(text('CREATE TABLE students_new (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)'))  # Create new students table
            connection.execute(text('INSERT INTO students_new (id, name, email) SELECT id, name, email FROM students'))  # Copy existing records
            connection.execute(text('DROP TABLE students'))  # Drop old table
            connection.execute(text('ALTER TABLE students_new RENAME TO students'))  # Rename new table
    # Restore relationships from the temporary table
    if 'student_courses_temp' in metadata.tables:
        with engine.connect() as connection:
            connection.execute(text('INSERT INTO student_courses (student_id, course_id) SELECT student_id, course_id FROM student_courses_temp'))  # Restore relationships
            connection.execute(text('DROP TABLE student_courses_temp'))  # Drop temp table after restoring
    # Add migration for student_courses table if it doesn't exist
    if 'student_courses' not in metadata.tables:
        with engine.connect() as connection:
            connection.execute(text('CREATE TABLE student_courses (student_id INTEGER, course_id INTEGER, PRIMARY KEY (student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(course_id) REFERENCES courses(id))'))  # Create association table
if __name__ == "__main__":
    migrate()