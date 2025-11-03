from sqlalchemy import Column, Integer, Table, ForeignKey
from db.database import Base

# Association table for many-to-many relationship between students and courses
student_courses_table = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

def create_student_courses_table():
    """
    Creates the student_courses association table in the database.
    This function should be called as part of the database initialization process.
    """
    try:
        # Creates all tables defined in Base.metadata, including the student_courses table
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        # Log the exception with a message
        print(f"Error creating tables: {e}")
        raise  # Reraise the exception for visibility in the application logs

# Expose the association table, if needed by other parts of the application
__all__ = ['student_courses_table']