'''
Handles database connections and session management.
'''
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, Session
from base import Base  # Import Base from the new base module
from models import Teacher  # Import Teacher from models
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
    metadata = MetaData(bind=engine)
    # Create the teachers table if it does not exist
    if 'teachers' not in metadata.tables:
        Teacher.__table__.create(bind=engine)
    # Ensure students and courses tables exist
    if 'students' not in metadata.tables:
        Student.__table__.create(bind=engine)
    if 'courses' not in metadata.tables:
        Course.__table__.create(bind=engine)
    # Ensure the student_courses table exists
    if 'student_courses' not in metadata.tables:
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