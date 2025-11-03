'''
Handles the migration of the database to include the Course table.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course  # Import the Course model
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
# Create a session
session = SessionLocal()
# Create the tables if they don't exist
Base.metadata.create_all(engine)  # This should create both Student and Course tables
# Commit the changes
session.commit()
session.close()