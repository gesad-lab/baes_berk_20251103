from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_URL = "sqlite:///students.db"  # Use SQLite for local development
engine = create_engine(DATABASE_URL)

def init_db():
    """
    Initializes the database by creating the necessary tables.
    The tables will only be created if they do not already exist.
    """
    try:
        # Create all tables in the database
        Base.metadata.create_all(engine)
        logger.info("Database initialized successfully.")
    except Exception as e:
        # Log the exception with context for debugging
        logger.error(f"Failed to initialize the database: {e}")

# Call the initialization logic on import
init_db()