```python
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Base class for all models
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

# Migration script to add email column in students table
def add_email_column_to_students(engine):
    """Run migration to add email column to students table."""
    with engine.connect() as connection:
        connection.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT '';")

# Migration script configuration
def run_migration():
    # Connection to the database
    DATABASE_URL = "sqlite:///./db.sqlite3"  # Update this with your actual database URL
    engine = create_engine(DATABASE_URL)
    
    # Run migration
    add_email_column_to_students(engine)

if __name__ == "__main__":
    run_migration()
```