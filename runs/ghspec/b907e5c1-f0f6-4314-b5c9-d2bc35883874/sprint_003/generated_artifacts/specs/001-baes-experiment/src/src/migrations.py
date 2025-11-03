```python
# src/migrations.py

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from your_application.database import get_database_uri  # Function to get DB URI from config

Base = declarative_base()  # Base class for declarative model definitions

class Course(Base):
    """Course model for database."""
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Course name is required
    level = Column(String, nullable=False)  # Course level is required

def migrate_create_courses_table():
    """Create the courses table in the database if it doesn't already exist."""
    try:
        # Create database engine and session
        engine = create_engine(get_database_uri())
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Create the courses table
        Base.metadata.create_all(engine)

        # Commit the changes
        session.commit()
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Migration failed: {e}")  # Log error for debugging
    finally:
        session.close()  # Ensure the session is closed

if __name__ == "__main__":
    migrate_create_courses_table()  # Run migration if this module is executed directly
```