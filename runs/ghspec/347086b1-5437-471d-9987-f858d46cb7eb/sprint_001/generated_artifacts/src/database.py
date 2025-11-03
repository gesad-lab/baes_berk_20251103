```python
# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base

# Database URL for SQLite database
DATABASE_URL = "sqlite:///./students.db"

# Create a SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create tables if they don't exist."""
    try:
        # Create all tables in the engine. This will create the tables if they do not already exist.
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        # Log the error with appropriate context for debugging
        print(f"Error initializing the database: {e}")  # In production, consider using logging framework

```