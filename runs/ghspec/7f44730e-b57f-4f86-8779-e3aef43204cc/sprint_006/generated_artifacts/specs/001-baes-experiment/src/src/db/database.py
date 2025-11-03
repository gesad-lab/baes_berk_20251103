```python
# src/db/database.py
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

DATABASE_URL = "sqlite:///./education.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define base class for SQLAlchemy models
Base = declarative_base()

# Existing Course model
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)  # New teacher_id foreign key

# New Teacher model
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)  # Create Course and Teacher tables

    # Additional logic for data migration or restrictions can be added here
    # Handling potential existing data or other migration processes can be added in future migrations
    try:
        pass  # Place for any necessary migration logic in the future
    except IntegrityError:
        # Log the integrity error and handle it properly
        print("Integrity error occurred during database initialization. Check existing data.")
```