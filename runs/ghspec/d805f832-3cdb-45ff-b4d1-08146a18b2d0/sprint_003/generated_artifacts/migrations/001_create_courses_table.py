from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for declarative models
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name of the Course
    level = Column(String, nullable=False)  # Level of the Course

# Database connection setup
DATABASE_URL = "sqlite:///./database.db"  # Assuming SQLite for local development
engine = create_engine(DATABASE_URL)

def run_migration():
    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    run_migration()  # Execute the migration script directly if this module is run
