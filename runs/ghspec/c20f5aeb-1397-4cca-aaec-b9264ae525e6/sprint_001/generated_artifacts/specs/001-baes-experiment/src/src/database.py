from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Student model that represents the 'students' table in the database."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def initialize_database(db_url: str):
    """Initialize the database and create tables if they do not exist.

    Args:
        db_url (str): The database URL for the SQLite database.
    """
    try:
        # Create a database engine
        engine = create_engine(db_url)

        # Create all tables in the database which are defined by the Base subclasses
        Base.metadata.create_all(engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        return Session()
    except Exception as e:
        # Log the exception or handle it accordingly
        print(f"Error initializing the database: {str(e)}")
        raise