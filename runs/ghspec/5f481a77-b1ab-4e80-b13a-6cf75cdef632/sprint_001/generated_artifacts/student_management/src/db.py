```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Set up the base class for declarative models
Base = declarative_base()

# Database connection string (should ideally be loaded from a config)
DATABASE_URL = "sqlite:///students.db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Function to initialize the database schema
def init_db():
    # Import all modules here to ensure they are registered correctly
    from .models import Student  # Import the Student model
    Base.metadata.create_all(engine)  # Create the database tables

# This is the end of the current file content.
```