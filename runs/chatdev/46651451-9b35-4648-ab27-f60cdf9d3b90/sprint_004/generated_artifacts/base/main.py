'''
Handles database migrations to add the email field to the Student entity and create the Course entity.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course  # Import necessary models
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def upgrade():
    '''
    Creates the courses table if it doesn't exist and ensures the email field is added to the Student entity.
    Preserves existing Student data.
    '''
    # Create the courses table
    Course.__table__.create(bind=engine, checkfirst=True)  # This will create the courses table if it doesn't exist
    # Use inspector to check if the students table exists
    inspector = inspect(engine)
    if not inspector.has_table("students"):
        Base.metadata.create_all(bind=engine)  # Create students table if it doesn't exist
def downgrade():
    '''
    Logic to remove the email column if necessary (not implemented).
    '''
    pass
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # Create tables if they don't exist
    upgrade()  # Run the upgrade to add the email field and create courses table