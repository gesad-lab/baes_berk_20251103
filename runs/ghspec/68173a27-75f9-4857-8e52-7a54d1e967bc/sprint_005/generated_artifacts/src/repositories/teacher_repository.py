```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setting up the SQL Alchemy Base
Base = declarative_base()

class Teacher(Base):
    """
    Teacher entity representation for database.
    
    Attributes:
      id (int): Unique identifier for the teacher.
      name (str): Name of the teacher.
      email (str): Unique email of the teacher.
    """
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Database connection
DATABASE_URL = "sqlite:///./test.db"  # Example configuration, replace with actual DB URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_teacher_table():
    """
    Create the teachers table in the database if it does not exist.
    This migration function handles creating the table structure.
    """
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Execute the migration script
    create_teacher_table()
```