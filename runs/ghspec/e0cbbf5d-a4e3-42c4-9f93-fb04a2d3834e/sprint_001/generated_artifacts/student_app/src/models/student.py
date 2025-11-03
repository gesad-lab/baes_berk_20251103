```python
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative model definitions
Base = declarative_base()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///students.db")

# Create an SQLite database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create the database tables if they don't already exist."""
    # Import all modules here that might define models so that
    # they will be registered on the metadata before creating the tables
    from src.models.student import Student  # Import the Student model
    
    # Create the database tables
    Base.metadata.create_all(bind=engine)

# Run the database initialization on module import
if __name__ == "__main__":
    init_db()
```