'''
Migration script to create the Course table and add email field to the Student table.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Student, Course  # Import the models to ensure migration is aware of them
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Create the migration
def migrate():
    # Create the tables if they do not exist
    Base.metadata.create_all(bind=engine)
if __name__ == "__main__":
    migrate()