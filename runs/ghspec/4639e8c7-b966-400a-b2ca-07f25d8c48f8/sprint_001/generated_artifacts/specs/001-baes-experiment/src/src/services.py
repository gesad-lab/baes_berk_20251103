```python
from typing import List, Optional
from flask import jsonify, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

# Create a base class for our ORM models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Initialize the database connection and create the tables
def init_db(database_url: str):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

# Business logic for student operations
class StudentService:
    def __init__(self, db_session: Session):
        self.session = db_session

    def create_student(self, name: str) -> Optional[dict]:
        """Create a new student record with the provided name."""
        if not name:
            return {"error": {"code": "E001", "message": "Name cannot be empty."}}

        new_student = Student(name=name)
        self.session.add(new_student)
        
        try:
            self.session.commit()
            return {"id": new_student.id, "name": new_student.name}
        except IntegrityError:
            self.session.rollback()
            return {"error": {"code": "E002", "message": "Failed to create student record due to integrity constraints."}}

    def get_all_students(self) -> List[dict]:
        """Retrieve a list of all student records."""
        students = self.session.query(Student).all()
        return [{"id": student.id, "name": student.name} for student in students]

# Error handling for request data validation
def validate_student_input(data: dict) -> Optional[dict]:
    if 'name' not in data or not isinstance(data['name'], str) or not data['name'].strip():
        return {"error": {"code": "E001", "message": "Name is required and must be a non-empty string."}}
    return None
```