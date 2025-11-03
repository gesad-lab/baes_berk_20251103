from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating the Student table if it does not exist.
    
    This function should be called at application startup to ensure that the
    database schema is set up correctly before any data manipulation occurs.
    """
    from .models.student import Base  # Import the Base model for metadata
    Base.metadata.create_all(bind=engine)  # Create the tables in the database

# Call init_db to set up the database when the module is loaded
init_db()