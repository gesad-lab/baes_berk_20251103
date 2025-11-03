```python
# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.course import Base  # New import for Course model
from alembic import command
from alembic.config import Config

DATABASE_URL = "sqlite:///./courses.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating all tables defined in the models
    and running any available migrations.

    This function should be called at application startup to ensure that 
    the database schema is up to date.
    """
    try:
        # Create all tables, including newly added ones such as Course
        Base.metadata.create_all(bind=engine)  
        
        # Configuration for Alembic to handle migrations
        alembic_cfg = Config("alembic.ini")
        
        # Run migrations if available
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        # Log the error and raise an exception to avoid silent failures
        print(f"Error during database initialization and migration: {e}")
        raise
```