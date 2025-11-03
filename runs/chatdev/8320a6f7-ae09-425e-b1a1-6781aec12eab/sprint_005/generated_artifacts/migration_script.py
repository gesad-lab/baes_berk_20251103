'''
Handles the migration of the database to include the Teacher table.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base  # Import the Base to check for existing tables
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
# Create a session
session = SessionLocal()
# Check if the Teacher table already exists
inspector = inspect(engine)
if not inspector.has_table("teachers"):
    Base.metadata.tables['teachers'].create(engine)  # Create Teacher table only if it doesn't exist
# Commit the changes
session.commit()
session.close()