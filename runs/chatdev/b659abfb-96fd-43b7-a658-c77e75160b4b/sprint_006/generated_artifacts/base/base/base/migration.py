'''
Migration script to add Course table to the database.
This script ensures that the Course table is created without affecting existing Student data.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Course  # Import the Course model
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create the Course table if it does not exist
inspector = inspect(engine)
if 'courses' not in inspector.get_table_names():
    Course.__table__.create(bind=engine)  # Create only the Course table