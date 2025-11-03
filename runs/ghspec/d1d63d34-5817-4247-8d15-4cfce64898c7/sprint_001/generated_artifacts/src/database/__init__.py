from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for the SQLAlchemy ORM models
Base = declarative_base()

class Student(Base):
    """Model for the Student entity."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

def init_db(database_url: str):
    """
    Initializes the database by creating the schema.

    Args:
        database_url (str): The database connection URL.
    """
    # Create a new database engine instance
    engine = create_engine(database_url)

    # Create all tables in the engine (this creates the schema)
    Base.metadata.create_all(engine)

    # Optionally, create a session to interact with the database
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal

# Example initialization on application startup (this should be called during startup)
# init_db("sqlite:///./students.db")  # Uncomment to initialize with an SQLite database file