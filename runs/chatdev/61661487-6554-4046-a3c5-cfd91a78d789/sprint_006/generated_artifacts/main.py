'''
Database migration script to create Course and Teacher tables while preserving existing Student data.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Course, Teacher
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def migrate():
    inspector = inspect(engine)
    if 'courses' not in inspector.get_table_names() or 'teachers' not in inspector.get_table_names():
        Base.metadata.create_all(bind=engine)  # Create new Course and Teacher tables
    # Ensure existing data is preserved and relationships are established
    with SessionLocal() as session:
        existing_courses = session.query(Course).all()
        for course in existing_courses:
            # Set a default teacher_id or handle as necessary
            if course.teacher_id is None:
                course.teacher_id = 1  # Assuming a default teacher with ID 1 exists
        session.commit()
if __name__ == "__main__":
    migrate()