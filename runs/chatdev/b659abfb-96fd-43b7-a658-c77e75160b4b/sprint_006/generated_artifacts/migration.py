'''
Migration script to add Teacher table to the database.
This script ensures that the Teacher table is created without affecting existing Student and Course data.
'''
from sqlalchemy import create_engine, inspect, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import Teacher, Course  # Import the Course model
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_teacher_table():
    inspector = inspect(engine)
    if 'teachers' not in inspector.get_table_names():
        Teacher.__table__.create(bind=engine)  # Create only the Teacher table
def add_teacher_id_to_courses():
    inspector = inspect(engine)
    if 'courses' in inspector.get_table_names():
        # Check if the teacher_id column already exists
        if 'teacher_id' not in [column['name'] for column in inspector.get_columns('courses')]:
            with SessionLocal() as db:
                # Add the teacher_id column to the courses table
                db.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER')
                db.commit()
try:
    create_teacher_table()
    add_teacher_id_to_courses()
except Exception as e:
    print(f"Error during migration: {e}")