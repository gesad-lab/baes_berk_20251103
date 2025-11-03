from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

# Create a base class for declarative models
Base = declarative_base()

# Initialize the database engine (assuming some DATABASE_URL is defined)
DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

def init_db():
    """Initializes the database by creating all necessary tables and checking for the junction table."""
    # Create all tables defined by the Base subclasses
    Base.metadata.create_all(bind=engine)
    
    # Inspect the database to check for existing tables
    inspector = inspect(engine)
    
    # Check if the junction table for student-course association exists
    if "student_course_association" not in inspector.get_table_names():
        with engine.begin() as connection:
            # Create the junction table
            connection.execute('''CREATE TABLE student_course_association (
                                    student_id INTEGER,
                                    course_id INTEGER,
                                    PRIMARY KEY(student_id, course_id),
                                    FOREIGN KEY(student_id) REFERENCES students(id),
                                    FOREIGN KEY(course_id) REFERENCES courses(id)
                                  )''')
            # The use of foreign keys ensures referential integrity in the junction table

# Call init_db at the application startup point to ensure the schema is up-to-date
if __name__ == "__main__":
    init_db()