from sqlalchemy import Column, Integer, ForeignKey
from models import db, StudentCourses

def upgrade():
    """Create the student_courses table to establish many-to-many relationship between students and courses."""
    # Create the student_courses table with student_id and course_id as foreign keys
    db.create_table('student_courses', 
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    """Drop the student_courses table if needed."""
    db.drop_table('student_courses')  # Drop the linking table if it exists