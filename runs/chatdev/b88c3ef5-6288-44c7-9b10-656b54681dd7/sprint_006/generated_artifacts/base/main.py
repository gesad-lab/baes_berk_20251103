'''
Handles database migrations for the Student, Course, and Teacher entities.
'''
from sqlalchemy import create_engine, inspect
from models import Base, student_courses, Teacher
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def upgrade():
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
    # Use inspect to check if the student_courses table exists
    inspector = inspect(engine)
    if 'student_courses' not in inspector.get_table_names():
        student_courses.create(bind=engine)
    # Add the Teacher table creation
    if 'teachers' not in inspector.get_table_names():
        Teacher.__table__.create(bind=engine)
    # Ensure that existing Student and Course data is preserved
    if inspector.get_table_names() == ['students', 'courses', 'student_courses']:
        print("Existing Student and Course data is preserved.")
def downgrade():
    # Drop the Teacher table if it exists
    inspector = inspect(engine)
    if 'teachers' in inspector.get_table_names():
        Teacher.__table__.drop(bind=engine)
if __name__ == "__main__":
    upgrade()