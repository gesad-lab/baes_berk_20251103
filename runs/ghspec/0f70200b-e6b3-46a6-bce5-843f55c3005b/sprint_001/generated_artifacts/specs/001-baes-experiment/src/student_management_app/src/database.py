from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite
DATABASE_URL = "sqlite:///students.db"

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the Student model
class Student(Base):
    """Represents a student entity with a required name."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Student ID
    name = Column(String, nullable=False)  # Student name (required)

def init_db():
    """Initialize the SQLite database and create the schema if it does not exist."""
    # Create a new database engine
    engine = create_engine(DATABASE_URL)

    # Create the students table if it doesn't already exist
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Return a session to interact with the database
    return Session()