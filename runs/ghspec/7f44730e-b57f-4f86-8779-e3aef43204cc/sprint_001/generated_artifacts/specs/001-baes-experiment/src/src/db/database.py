```python
# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base

# Configuration for SQLite database connection
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialize the database schema by creating tables if they do not exist.
    
    This function is called on application startup to ensure that the 
    necessary database schema is set up before any operations are performed.
    """
    try:
        # Create all tables defined by the Base model 
        Base.metadata.create_all(bind=engine)
        print("Database schema initialized successfully.")
    except Exception as e:
        # Log error during initialization
        print(f"Error during database initialization: {str(e)}")
        # You could raise a custom exception here if needed
```