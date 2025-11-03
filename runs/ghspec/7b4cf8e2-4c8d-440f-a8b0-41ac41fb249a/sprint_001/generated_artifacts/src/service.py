```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional, Dict, Any

# Database setup
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Student model definition
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema
def init_db():
    Base.metadata.create_all(bind=engine)

# Service functions for CRUD operations
def create_student(name: str) -> Student:
    """Create a new student record."""
    if not name:
        raise ValueError("Student name is required.")

    session = SessionLocal()
    new_student = Student(name=name)
    
    try:
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        return new_student
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_student(student_id: int) -> Optional[Student]:
    """Retrieve a student record by ID."""
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        return student
    finally:
        session.close()

def update_student(student_id: int, name: str) -> Optional[Student]:
    """Update an existing student's name."""
    if not name:
        raise ValueError("Student name is required.")

    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            student.name = name
            session.commit()
            session.refresh(student)
            return student
        return None
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_student(student_id: int) -> bool:
    """Delete a student record by ID."""
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            session.delete(student)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
```