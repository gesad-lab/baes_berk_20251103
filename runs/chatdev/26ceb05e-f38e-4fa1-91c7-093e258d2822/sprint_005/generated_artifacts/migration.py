'''
Migration script to add the Teacher table to the database while preserving existing data.
'''
from sqlalchemy import create_engine, inspect
from models import Base  # Import Base to access the metadata
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Check if the Teacher table already exists
if not inspect(engine).has_table("teachers"):
    # Create the Teacher table if it does not exist
    Base.metadata.create_all(bind=engine, tables=[Base.metadata.tables['teachers']])