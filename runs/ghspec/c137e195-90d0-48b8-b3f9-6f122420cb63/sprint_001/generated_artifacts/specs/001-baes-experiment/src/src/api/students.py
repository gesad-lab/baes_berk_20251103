```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Student
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./students.db"

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  
Base = declarative_base()

def init_db():
    """
    Initialize the database and create the schema if it does not already exist.
    This function needs to be called at startup to ensure that the database 
    is set up correctly for the application to function.
    """
    # Create all tables in the database that are defined by Base subclasses
    Base.metadata.create_all(bind=engine)
    
# SessionLocal will be used to create new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

```