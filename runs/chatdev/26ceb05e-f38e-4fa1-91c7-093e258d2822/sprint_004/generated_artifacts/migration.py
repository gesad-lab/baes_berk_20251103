'''
Migration script to add the Course and Enrollment tables to the database.
'''
from sqlalchemy import create_engine, inspect
from models import Base  # Import Base to access the metadata
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create all tables if they do not exist
if not inspect(engine).has_table("enrollments"):
    Base.metadata.create_all(bind=engine)  # This will create the Course and Enrollment tables and preserve existing Student data