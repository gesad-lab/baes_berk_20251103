```python
import os
import logging
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///students.db')

# SQLAlchemy base model
Base = declarative_base()

class Student(Base):
    """Student model representing the students table in the database."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required name field

def init_db():
    """Initialize the database and create tables."""
    try:
        # Create a new database engine instance
        engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
        
        # Create all tables in the database (defined by Base subclasses)
        Base.metadata.create_all(engine)
        logger.info("Database initialized and tables created successfully.")
        
    except Exception as e:
        logger.error(f"An error occurred while initializing the database: {e}")
        raise

# Create a new session factory to interact with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(DATABASE_URL, connect_args={"check_same_thread": False}))

if __name__ == '__main__':
    init_db()  # Initialize the database on module run
```