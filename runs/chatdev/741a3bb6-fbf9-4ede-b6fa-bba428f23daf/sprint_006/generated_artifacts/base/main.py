'''
Migration script to create the Course and Teacher tables and add email field to the Student table.
'''
from sqlalchemy import create_engine, inspect, text  # Updated import to include text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Student, Course, Teacher  # Import the models to ensure migration is aware of them
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Create the migration
def migrate():
    # Create the tables if they do not exist
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)  # Use inspect to check for the table
    # Check if the association table already exists
    if not inspector.has_table('student_courses'):
        # Create the association table if it does not exist
        with engine.connect() as connection:
            connection.execute(
                text("CREATE TABLE student_courses (student_id INTEGER, course_id INTEGER, PRIMARY KEY (student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(course_id) REFERENCES courses(id))")
            )
    # Create Teacher table
    if not inspector.has_table('teachers'):
        with engine.connect() as connection:
            connection.execute(
                text("CREATE TABLE teachers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)")
            )
if __name__ == "__main__":
    migrate()