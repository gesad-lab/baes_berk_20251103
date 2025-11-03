from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base model for SQLAlchemy
Base = declarative_base()

class Student(Base):
    """Represents a student entity in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def initialize_database(db_uri: str) -> None:
    """
    Initializes the database by creating the necessary tables.

    Parameters:
        db_uri (str): The database URI for connection (e.g., SQLite path).

    Raises:
        Exception: Raises an exception if the database initialization fails.
    """
    try:
        # Create an engine that connects to the specified database
        engine = create_engine(db_uri)
        
        # Create all tables in the database which are defined by the Base classes
        Base.metadata.create_all(engine)
        
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize the database: {str(e)}")
        raise