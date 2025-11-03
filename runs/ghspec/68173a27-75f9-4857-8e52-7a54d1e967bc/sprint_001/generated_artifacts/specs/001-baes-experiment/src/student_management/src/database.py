```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
SQL_DATABASE_URL = "sqlite:///./students.db"  # SQLite database URL
engine = create_engine(SQL_DATABASE_URL, connect_args={"check_same_thread": False})  # Create the database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Create a session local class
Base = declarative_base()  # Create a declarative base for models

# Function to initialize the database schema
def init_db():
    import models.student  # Import models to create tables
    Base.metadata.create_all(bind=engine)  # Create database tables based on models
```