'''
Handles database migrations for adding Course and Teacher entities and email field to Student entity.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Teacher
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def upgrade():
    # Create Teacher table if it does not exist
    if not inspect(engine).has_table("teachers"):
        Teacher.__table__.create(bind=engine)
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
    # Ensure existing data in students and courses is preserved
    with SessionLocal() as session:
        existing_students = session.query(Student).all()
        existing_courses = session.query(Course).all()
        existing_teachers = session.query(Teacher).all()  # Fetch existing teachers
        # Print existing data for debugging
        print(f"Existing students: {existing_students}")
        print(f"Existing courses: {existing_courses}")
        print(f"Existing teachers: {existing_teachers}")
        # Assign a default teacher to existing courses if necessary
        if existing_teachers:
            default_teacher_id = existing_teachers[0].id  # Example: use the first teacher as default
            for course in existing_courses:
                if course.teacher_id is None:  # Only assign if no teacher is set
                    course.teacher_id = default_teacher_id
                    session.add(course)
            session.commit()  # Commit changes to the database
def downgrade():
    # Downgrade logic if needed
    pass
if __name__ == "__main__":
    upgrade()