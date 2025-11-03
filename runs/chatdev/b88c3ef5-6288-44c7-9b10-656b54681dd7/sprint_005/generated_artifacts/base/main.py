'''
Handles database migrations for the Student and Course entities.
'''
from sqlalchemy import create_engine, inspect
from models import Base, student_courses
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def upgrade():
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
    # Use inspect to check if the student_courses table exists
    inspector = inspect(engine)
    if 'student_courses' not in inspector.get_table_names():
        student_courses.create(bind=engine)
def downgrade():
    # Drop the association table if it exists
    inspector = inspect(engine)
    if 'student_courses' in inspector.get_table_names():
        student_courses.drop(bind=engine)
if __name__ == "__main__":
    upgrade()