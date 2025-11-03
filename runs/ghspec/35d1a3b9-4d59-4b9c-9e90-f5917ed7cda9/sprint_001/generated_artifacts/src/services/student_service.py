```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional

# Base class for SQLAlchemy models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Database connection setup
DATABASE_URL = 'sqlite:///students.db'  # SQLite database URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create the database schema
def init_db() -> None:
    """Create database tables if they do not exist."""
    Base.metadata.create_all(bind=engine)

# Service layer for student operations
class StudentService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_student(self, name: str) -> Student:
        """
        Create a new student in the database.
        
        :param name: Name of the student to be created.
        :return: The created Student object.
        """
        if not name:
            raise ValueError("Student name cannot be empty.")

        new_student = Student(name=name)
        try:
            self.db.add(new_student)
            self.db.commit()
            self.db.refresh(new_student)  # Refresh to get the new student with ID
        except SQLAlchemyError as e:
            self.db.rollback()  # Rollback in case of error
            raise RuntimeError("Error creating student: ") from e
            
        return new_student

    def get_students(self) -> List[Student]:
        """
        Retrieve all students from the database.
        
        :return: A list of Student objects.
        """
        try:
            return self.db.query(Student).all()
        except SQLAlchemyError as e:
            raise RuntimeError("Error retrieving students: ") from e

# Initialize the database schema on application startup
init_db()
```