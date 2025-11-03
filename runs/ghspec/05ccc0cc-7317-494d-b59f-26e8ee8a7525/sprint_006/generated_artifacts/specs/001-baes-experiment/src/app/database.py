```python
# app/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.models import Course, Teacher  # Import the Course and Teacher models

# Define the database URL
DATABASE_URL = "sqlite:///./test.db"  # Adjust accordingly for your environment

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a declarative base for ORM
Base = declarative_base()

# Create a new session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def run_migration():
    """ Run the database migration to add teacher_id to the Course table. """
    try:
        # Begin migration: add a 'teacher_id' column to the 'Course' table
        with engine.connect() as connection:
            # Perform the migration using an ALTER TABLE statement
            connection.execute("ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);")
    except SQLAlchemyError as e:
        print(f"Migration failed: {e}")

# Run migration on application startup
run_migration()
```