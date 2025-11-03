'''
Migration script to create the Course and Teacher tables and the association table.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Student, Course, Teacher  # Importing the Student, Course, and Teacher models
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def upgrade():
    """Create the courses and teachers tables while preserving existing data."""
    Base.metadata.create_all(bind=engine)  # This will create students, courses, and teachers tables
def downgrade():
    """Remove courses and teachers tables if needed."""
    # Implement logic to drop the courses and teachers tables safely
    pass
if __name__ == "__main__":
    upgrade()