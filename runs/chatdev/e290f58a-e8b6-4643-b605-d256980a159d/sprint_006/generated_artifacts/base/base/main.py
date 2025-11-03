'''
Migration script to create the Course table and the association table.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Student, Course  # Importing the Student and Course models
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def upgrade():
    """Create the courses table and the association table while preserving existing data."""
    # Create the new tables
    Base.metadata.create_all(bind=engine)  # This will create both students and courses tables
    # Here you would implement logic to migrate existing student data if necessary
    # For example, you could copy existing student records to a temporary table
    # and then back to the new structure if needed.
def downgrade():
    """Remove courses table and association table if needed."""
    # Implement logic to drop the courses and association tables safely
    # This may involve checking for existing data and handling it appropriately.
    pass
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)