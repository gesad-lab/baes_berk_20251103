```python
# src/services/enrollment_service.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table

# Base class for SQLAlchemy models
Base = declarative_base()

# Define the join table for student_courses
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    # Relationships for ORM
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Function to create the migration script
def create_student_courses_table(engine):
    """Create the student_courses join table in the database."""
    Base.metadata.create_all(engine)

# Example usage:
# database_url = 'sqlite:///your_database.db'  # Use your specific database URL
# engine = create_engine(database_url)
# create_student_courses_table(engine)

# The following code can be added to your migration script execution setup
if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine

    database_url = os.getenv("DATABASE_URL", "sqlite:///default.db")
    engine = create_engine(database_url)

    # Create the student_courses table
    create_student_courses_table(engine)
    print("Migration completed: student_courses table created.")
```