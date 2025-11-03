```python
# src/models/student.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for SQLAlchemy models
Base = declarative_base()

class Student(Base):
    """Represents a student in the database."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name is a required field

# Database configuration
DATABASE_URL = "sqlite:///./students.db"  # SQLite database URL

# Create a new SQLite database (or connect to an existing one)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database by creating the tables."""
    Base.metadata.create_all(bind=engine)  # Create all tables defined in the models

# Call init_db to ensure the database schema is created on startup
if __name__ == '__main__':
    init_db()
```