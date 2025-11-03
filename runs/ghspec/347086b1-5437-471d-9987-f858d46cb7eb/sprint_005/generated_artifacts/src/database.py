```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

Base = declarative_base()

DATABASE_URL = "sqlite:///./test.db"  # Replace with actual database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(bind=engine)

def get_teacher(db_session, teacher_id: int):
    """Retrieve a Teacher by ID."""
    return db_session.query(Teacher).filter(Teacher.id == teacher_id).first()

def create_teacher(db_session, name: str, email: str):
    """Create a new Teacher entity in the database."""
    if not name or not email:
        raise HTTPException(status_code=400, detail="Both name and email are required.")
    
    new_teacher = Teacher(name=name, email=email)
    db_session.add(new_teacher)
    
    try:
        db_session.commit()
        db_session.refresh(new_teacher)
        return new_teacher
    except IntegrityError:
        db_session.rollback()
        raise HTTPException(status_code=400, detail="A teacher with this email already exists.")
```
