```python
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "context": "%(name)s"}'
)
logger = logging.getLogger(__name__)

# Define the base class for ORM
Base = declarative_base()

# Database configuration
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Student(Base):
    """Student entity with ORM functionality."""
    
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)  # Assuming an ID is needed
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)  # New email field

    def __init__(self, name: str, email: str):
        if not name:
            logger.error('Failed to create student: name is required', extra={'context': 'Student'})
            raise ValueError('Name is required')
        self.name = name
        self.email = email

def init_db():
    """Initialize the database and apply migrations."""
    try:
        # Create the database tables, including any new ones
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized and schema applied.")
    except Exception as e:
        logger.error("Database initialization failed: %s", str(e), extra={'context': 'Database'})
        raise

# Call to initialize the database when the application starts
init_db()
```