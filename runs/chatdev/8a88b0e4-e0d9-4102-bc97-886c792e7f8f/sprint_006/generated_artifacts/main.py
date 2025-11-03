'''
Migration script to create Course and Teacher tables, create association table, and ensure email column exists in the Student table.
'''
from sqlalchemy import create_engine, text
from models import Base, Teacher  # Import Teacher class
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def create_tables():
    '''
    Creates the necessary tables in the database, including the Course and Teacher tables and the association table.
    '''
    Base.metadata.create_all(engine)  # This will create students, courses, teachers, and the association table
def add_email_column():
    '''
    Adds the email column to the students table.
    The email column is added with a default value to preserve existing data.
    '''
    with engine.connect() as connection:
        # Check if the email column already exists
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            # Add email column as nullable initially to preserve existing data
            connection.execute(text("ALTER TABLE students ADD COLUMN email TEXT DEFAULT ''"))  # Set default value
        else:
            print("Email column already exists, skipping addition.")
def add_teacher_id_column():
    '''
    Adds the teacher_id column to the courses table.
    The teacher_id column is added as nullable initially to preserve existing data.
    '''
    with engine.connect() as connection:
        # Check if the teacher_id column already exists
        result = connection.execute(text("PRAGMA table_info(courses)"))
        columns = [row[1] for row in result]
        if 'teacher_id' not in columns:
            # Add teacher_id column as nullable initially to preserve existing data
            connection.execute(text("ALTER TABLE courses ADD COLUMN teacher_id INTEGER"))  # Add teacher_id column
        else:
            print("teacher_id column already exists, skipping addition.")
if __name__ == "__main__":
    create_tables()  # Ensure tables are created before migration
    add_email_column()
    add_teacher_id_column()  # Add migration for teacher_id