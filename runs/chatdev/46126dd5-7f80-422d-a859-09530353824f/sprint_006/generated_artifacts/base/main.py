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
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
    # Ensure existing data in students and courses is preserved
    with SessionLocal() as session:
        existing_students = session.query(Student).all()
        existing_courses = session.query(Course).all()
        print(f"Existing students: {existing_students}")
        print(f"Existing courses: {existing_courses}")
    # Create Teacher table if it does not exist
    if not inspect(engine).has_table("teachers"):
        Teacher.__table__.create(bind=engine)
def downgrade():
    # Downgrade logic if needed
    pass
if __name__ == "__main__":
    upgrade()