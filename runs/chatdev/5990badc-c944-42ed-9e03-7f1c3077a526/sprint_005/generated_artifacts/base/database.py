'''
Database connection and session management.
'''
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Course, Student  # Import models for migration
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Association table for the many-to-many relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
def create_database():
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def upgrade_database():
    # This function will handle the migration to add the Course table
    if not engine.dialect.has_table(engine, "courses"):  # Check if the 'courses' table exists
        Course.__table__.create(bind=engine)  # Explicitly create the Course table
    if not engine.dialect.has_table(engine, "student_courses"):  # Check if the association table exists
        student_courses.create(bind=engine)  # Create the association table
    # Logic to migrate existing data (if applicable)
    db = SessionLocal()
    try:
        existing_students = db.query(Student).all()
        for student in existing_students:
            # Assuming you have a way to get the courses for each student
            # This is a placeholder for actual logic to fetch courses
            courses_for_student = []  # Replace with actual logic to fetch courses
            for course in courses_for_student:
                db.execute(student_courses.insert().values(student_id=student.id, course_id=course.id))
        db.commit()
    finally:
        db.close()