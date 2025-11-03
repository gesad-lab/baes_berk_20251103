from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table

# Define the base for SQLAlchemy models
Base = declarative_base()

# Define the Student model (assuming it exists in models.py)
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)  # Assuming a primary key
    name = Column(String)  # Add other fields as necessary

# Define the Course model (assuming it exists in models.py)
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)  # Assuming a primary key
    name = Column(String)  # Add other fields as necessary

# Define the association table for Student and Course relationships
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Define the connection to the database
DATABASE_URL = "sqlite:///./test.db"  # Use your actual database URL
engine = create_engine(DATABASE_URL)

# Create a new session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create the database tables."""
    Base.metadata.create_all(bind=engine)  # Create all tables including the new student_courses table

# Handle migration logic
def migrate():
    """Perform database migration to ensure student_courses table is created."""
    # Here you'd check if the `student_courses` table exists and create if not,
    # but for simplicity, we are calling create_all which handles all necessary tables
    init_db()  # Call the function to create new tables

# Call migration on startup
if __name__ == "__main__":
    migrate()  # Initialize migration when this file is executed directly

# This file sets up the database connection, initializes the DB schema,
# and prepares for handling enrollments by creating necessary tables.