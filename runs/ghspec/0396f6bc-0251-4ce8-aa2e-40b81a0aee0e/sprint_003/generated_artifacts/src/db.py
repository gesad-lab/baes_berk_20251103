```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the base class for declarative models
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

def initialize_database(db_url: str):
    """
    Initializes the database by creating the necessary tables.
    
    Args:
        db_url (str): The database URL for the SQLite database.
    """
    engine = create_engine(db_url)
    
    # Create all tables in the database which are defined by Base subclasses
    Base.metadata.create_all(engine)  # This handles the creation of the courses table

# This function can be called in the application startup to ensure the database is ready
```