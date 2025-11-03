```python
# File: db/database.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.teacher import Teacher  # Importing the Teacher model

# Setting up database engine and base
DATABASE_URL = "sqlite:///./test.db"  # Adjust path as necessary
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_schema():
    """Create the database schema for the application."""
    Base.metadata.create_all(bind=engine)  # This will create all tables, including the teachers table

# Define the main metadata object
metadata = MetaData()

# Create schema at application startup
if __name__ == "__main__":
    create_schema()
```