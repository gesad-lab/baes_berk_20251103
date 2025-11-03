from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    """Represents a student entity with a name field."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

def initialize_database(db_uri: str) -> None:
    """Initializes the database and creates the schema if it does not exist.

    Args:
        db_uri (str): The database URI for the SQLite database.
    """
    try:
        # Create the database engine
        engine = create_engine(db_uri)

        # Create all tables in the engine
        Base.metadata.create_all(engine)
        print("Database initialized and schema created.")
    except Exception as e:
        # Log the error and re-raise with a user-friendly message
        print("Error initializing database: ", str(e))
        raise RuntimeError("Failed to initialize the database. Check your configuration.") from e