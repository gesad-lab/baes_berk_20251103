```python
# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base
from alembic import command
from alembic.config import Config

DATABASE_URL = "sqlite:///./students.db"

# Creating the database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating the necessary tables
    and applying any pending migrations.
    """
    # Create all tables defined in the Base's subclasses
    Base.metadata.create_all(bind=engine)
    
    # Set up Alembic configuration for database migrations
    alembic_cfg = Config("alembic.ini")
    
    # Run migrations to ensure the database schema is up to date
    command.upgrade(alembic_cfg, "head")  # Upgrade to the latest migration
```