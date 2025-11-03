'''
Database migration script to add Course table and email field to Student entity.
'''
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import Session
from models import Student, Course
from sqlalchemy import inspect
student_courses = Table(
    'student_courses',
    Student.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
def upgrade(db: Session):
    # Add email column to the existing Student table as nullable first
    with db.begin():
        # Check if the email column already exists to avoid errors
        if not db.has_table('students'):
            raise Exception("Students table does not exist.")
        # Check if the email column exists
        inspector = inspect(db.bind)
        columns = [column['name'] for column in inspector.get_columns('students')]
        if 'email' not in columns:
            # Add email column to the existing Student table
            db.execute('ALTER TABLE students ADD COLUMN email VARCHAR')
    # Create Course table
    Course.__table__.create(bind=db.bind, checkfirst=True)
    # Create association table for Student and Course
    student_courses.create(bind=db.bind, checkfirst=True)
def downgrade(db: Session):
    # Logic to remove the email column if needed
    pass