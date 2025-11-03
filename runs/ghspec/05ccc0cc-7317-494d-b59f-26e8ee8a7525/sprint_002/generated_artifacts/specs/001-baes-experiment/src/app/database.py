```python
import os
import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
from app.models import Base
from app.mixins import MigrationHandler  # Assuming you have a MigrationHandler for migration logic

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database URL configuration (using SQLite for local development)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def initialize_database():
    """
    Initialize the database by creating tables and handling migrations.
    This should be called at application startup.
    """
    metadata = MetaData(bind=engine)

    # Create tables if they don't exist yet
    try:
        if not database_exists(DATABASE_URL):  # Assuming a method to check if the database exists
            logger.info("Creating database and applying initial migrations...")
            Base.metadata.create_all(bind=engine)
            apply_migrations()
        else:
            logger.info("Database exists, checking for migrations...")
            apply_migrations()  # Apply any pending migrations
    except SQLAlchemyError as e:
        logger.error(f"Error during database initialization: {e}")
        raise

def apply_migrations():
    """
    Apply any schema migrations. This function should handle the logic
    to ensure that the database schema is updated according to the latest specifications.
    """
    migration_handler = MigrationHandler(engine)
    try:
        migration_handler.apply_pending_migrations()  # Implement the migration logic here
        logger.info("Database migrations applied successfully.")
    except Exception as e:
        logger.error(f"Error applying migrations: {e}")
        raise

def database_exists(url: str) -> bool:
    """
    Check if the database already exists.
    
    Args:
        url (str): The connection URL for the database.
    
    Returns:
        bool: True if the database exists, else False.
    """
    # Implement logic to check for database existence
    # This could involve trying to connect or query it
    return False  # Placeholder return value

# Call initialize_database on application startup
initialize_database()
```