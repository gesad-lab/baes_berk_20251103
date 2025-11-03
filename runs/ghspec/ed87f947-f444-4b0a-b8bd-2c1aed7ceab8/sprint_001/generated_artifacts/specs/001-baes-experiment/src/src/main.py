```python
import os
import logging
from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Define constants for the database URL
DATABASE_URL = "sqlite:///./students.db"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastAPI instance
app = FastAPI()

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize metadata
metadata = MetaData()

# Function to initialize the database
def init_db():
    """Initialize the SQLite database/schema on startup."""
    try:
        # Check if the database file already exists
        if not os.path.exists("students.db"):
            # Create the database schema (this is a placeholder, replace with actual ORM model creation)
            # For example: Base.metadata.create_all(bind=engine)
            logger.info("Creating the database schema.")
            # Assuming you have models defined, call the create_all method here.
            logger.info("Database schema created successfully.")
        else:
            logger.info("Database schema already exists.")
    except Exception as e:
        logger.error(f"Failed to initialize the database: {str(e)}")
        raise

# Call the initialization function on startup
@app.on_event("startup")
async def startup_event():
    """Event handler to run during application startup."""
    init_db()

# Define API endpoints for Student entity here
# ...

# Define other functions or classes as needed
# ...
```