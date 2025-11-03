'''
Handles the migration of the database to include the Course table and the association table.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base  # Import the Base to check for existing tables
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
# Create a session
session = SessionLocal()
# Check if tables already exist
inspector = inspect(engine)
if not inspector.has_table("students"):
    Base.metadata.create_all(engine)  # This should create both Student and Course tables and the association table
# Commit the changes
session.commit()
session.close()