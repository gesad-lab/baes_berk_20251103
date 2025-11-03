```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from .models import Base  # Assuming the Base is defined in models.py
import os

# Database URL can be sourced from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

def init_db():
    """Initialize the database and run migrations."""
    # Create a database engine
    engine = create_engine(DATABASE_URL)
    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Configure Alembic
    alembic_cfg = Config("alembic.ini")

    # Run migrations
    with engine.begin() as connection:
        command.upgrade(alembic_cfg, "head")  # Upgrade database to the latest revision

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    return Session()
```