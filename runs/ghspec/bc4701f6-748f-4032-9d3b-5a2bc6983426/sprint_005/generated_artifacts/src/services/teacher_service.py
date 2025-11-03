```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.models.student import Student  # Assuming there is an existing Student model
from src.models.course import Course  # Assuming there is an existing Course model

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"

def initialize_database():
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)  # Create all tables including Teacher

def create_teacher(db_session, name: str, email: str):
    """Create a new teacher record in the database."""
    if not name or not email:
        raise ValueError("Both name and email fields are required.")
    
    new_teacher = Teacher(name=name, email=email)
    db_session.add(new_teacher)
    db_session.commit()
    db_session.refresh(new_teacher)
    return new_teacher

def get_teacher(db_session, teacher_id: int):
    """Retrieve a teacher's information by ID."""
    teacher = db_session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise ValueError(f"Teacher with id {teacher_id} not found.")
    return teacher
```