```python
# /src/database/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
import os

# Create a base class for declarative models
Base = declarative_base()

# Create an engine that connects to the database; the connection string can be adjusted according to your database setup.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")  # Default to SQLite for local development
engine = create_engine(DATABASE_URL)

def init_db() -> None:
    """Initializes the database and creates the necessary schema for the application."""
    try:
        # Create all tables in the database by issuing the CREATE TABLE command
        Base.metadata.create_all(bind=engine)
        print("Database schema created successfully.")
    except SQLAlchemyError as e:
        # Handle any SQLAlchemy errors that occur during the schema creation process
        print(f"Error while creating database schema: {str(e)}")
```
