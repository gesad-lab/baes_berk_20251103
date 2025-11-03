```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
import os

Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL")

# Add Teacher model import if exists
from src.models import Teacher  # Assuming Teacher model is defined in models.py

def init_db():
    """Initializes the database, creating tables and applying migrations."""
    engine = create_engine(DATABASE_URL)
    
    # Bind the engine to the Base
    Base.metadata.bind = engine
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()
    
    # Check if the tables already exist, if not, create them
    if not database_exists(engine.url):
        Base.metadata.create_all(engine)  # Create all tables including the Teacher table

    # Perform migrations
    alembic_cfg = Config('alembic.ini')
    alembic_cfg.set_main_option('sqlalchemy.url', DATABASE_URL)
    command.upgrade(alembic_cfg, 'head')  # Upgrade to the latest migration

    # Close the session after completing the initialization
    session.close()

def database_exists(url):
    """Check if the database at the given URL already exists.

    Args:
        url (str): The database URL.

    Returns:
        bool: True if the database exists, False otherwise.
    """
    # Implement this function based on your database backend to check existence
    # For example, you may need to query the database or catch exceptions.
    pass
```