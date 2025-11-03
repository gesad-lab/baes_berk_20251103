```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field for teacher reference

    teacher = relationship("Teacher", back_populates="courses")  # Relationship to the Teacher model

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    courses = relationship("Course", back_populates="teacher")  # Link back to courses

def initialize_database(db_url: str):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # This handles the creation of the updated `courses` table along with existing tables
```