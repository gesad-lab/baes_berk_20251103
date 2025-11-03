from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """
    Represents a student entity in the database.
    
    Attributes:
        id (int): The unique identifier for a student.
        name (str): The name of the student, which is required.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def init_db(database_url: str):
    """
    Initialize the database and create the necessary tables.
    
    Args:
        database_url (str): The URL for the database connection.
    """
    try:
        # Create the database engine
        engine = create_engine(database_url)

        # Create all tables defined by Base subclasses
        Base.metadata.create_all(engine)

        # Set up a session
        Session = sessionmaker(bind=engine)
        return Session()  # Return a session for database interactions
    except Exception as e:
        # Log the error with context
        print(f"Error initializing database: {str(e)}")  # Should be replaced with a logging mechanism in production
        raise e  # Re-raise the exception for the caller to handle

# Note: The application should call init_db with the appropriate database URL to initialize the database at startup.