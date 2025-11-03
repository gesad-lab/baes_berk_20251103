```python
import logging
from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models.student import Student
from db.database import Base

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "context": "%(name)s"}'
)
logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def migrate_database():
    """Check and apply migrations to the database as necessary."""
    try:
        # Reflect the existing database schema
        metadata = MetaData(bind=engine)
        metadata.reflect()

        # Check if the 'students' table exists and needs the 'email' column
        if 'students' in metadata.tables:
            # Get the existing table
            students_table = metadata.tables['students']

            # Check for the 'email' column
            if 'email' not in students_table.columns:
                # Perform the migration to add the new 'email' column
                with engine.connect() as conn:
                    conn.execute('ALTER TABLE students ADD COLUMN email STRING;')
                    logger.info("Migration applied: 'email' column added to 'students' table.")
        else:
            logger.error("Migration error: 'students' table does not exist.")
    except SQLAlchemyError as e:
        logger.error(f"Database migration failed: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error during migration: {str(e)}")
        
# Apply the migration at startup
migrate_database()

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)  # This will include the email field when creating the table for the first time.
```