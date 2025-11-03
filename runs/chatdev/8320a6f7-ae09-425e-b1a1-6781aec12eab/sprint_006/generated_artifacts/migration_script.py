'''
Handles the migration of the database to include the Teacher table and update Course table.
'''
from sqlalchemy import create_engine, inspect, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import Base, Course  # Import the Base and Course to check for existing tables
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
# Create a session
session = SessionLocal()
# Check if the Teacher table already exists
inspector = inspect(engine)
if not inspector.has_table("teachers"):
    Base.metadata.tables['teachers'].create(engine)  # Create Teacher table only if it doesn't exist
# Check if the teacher_id column exists in the courses table
if not inspector.has_column("courses", "teacher_id"):
    with engine.connect() as connection:
        connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER;')  # Add teacher_id column
# Commit the changes
session.commit()
session.close()