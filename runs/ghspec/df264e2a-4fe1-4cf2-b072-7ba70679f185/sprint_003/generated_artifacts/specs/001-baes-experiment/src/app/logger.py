```python
# app/logger.py

import logging
from sqlalchemy import create_engine
from alembic import command
from alembic.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_migrations():
    """Run database migrations on startup."""
    # Specify database URL from environment settings
    database_url = "sqlite:///path_to_your_database.db"  # Update this line with actual config
    engine = create_engine(database_url)
    
    # Create Alembic configuration object
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.attributes['connection'] = engine

    # Run migrations
    try:
        logger.info("Starting database migrations...")
        with engine.begin() as connection:
            command.upgrade(alembic_cfg, "head")  # Migrate to the latest version
        logger.info("Database migrations completed successfully.")
    except Exception as e:
        logger.error(f"Error during database migrations: {e}")
        raise RuntimeError("Database migrations failed")

if __name__ == "__main__":
    # Run migrations before starting the server
    run_migrations()
    # Code to start the server goes here
```