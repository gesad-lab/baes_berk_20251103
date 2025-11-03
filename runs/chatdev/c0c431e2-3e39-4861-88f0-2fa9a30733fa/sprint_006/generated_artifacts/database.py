'''
Handles database connections and session management.
'''
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey, inspect
from sqlalchemy.orm import sessionmaker, Session
from base import Base  # Import Base from the new base module
from models import Teacher, Course  # Import Teacher and Course from models
# Define the association table here to avoid circular import
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_database():
    '''
    Creates the database and tables if they do not exist.
    '''
    Base.metadata.create_all(bind=engine)  # Create tables first
    migrate_database()  # Then perform migration
def migrate_database():
    '''
    Migrates the database to add the Teacher table and preserve existing Student and Course data.
    '''
    inspector = inspect(engine)
    # Create the teachers table if it does not exist
    if not inspector.has_table('teachers'):
        Teacher.__table__.create(bind=engine)
    # Ensure students and courses tables exist
    if not inspector.has_table('students'):
        Student.__table__.create(bind=engine)
    if not inspector.has_table('courses'):
        Course.__table__.create(bind=engine)
    # Check if the teacher_id column exists in the courses table
    if 'teacher_id' not in Course.__table__.columns:
        with engine.connect() as connection:
            connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id)')
    # Ensure the student_courses table exists
    if not inspector.has_table('student_courses'):
        student_courses.create(bind=engine)
def get_db() -> Session:
    '''
    Provides a database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()