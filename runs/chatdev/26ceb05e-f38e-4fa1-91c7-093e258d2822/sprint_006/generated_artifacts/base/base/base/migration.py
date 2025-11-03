'''
Migration script to add the Course table to the database.
'''
from sqlalchemy import create_engine
from models import Base  # Import Base to access the metadata
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create all tables if they do not exist
Base.metadata.create_all(bind=engine)  # This will create the Course table and preserve existing Student data