'''
Migration script to add email field to the Student table.
'''
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Student  # Import the Student model to ensure migration is aware of it
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Create the migration
def migrate():
    Base.metadata.create_all(bind=engine)
if __name__ == "__main__":
    migrate()