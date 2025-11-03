```python
# src/migrations/migration_add_teacher_to_course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Course model to store course information, now including teacher relationship."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key to Teacher

    # Relationship to Teacher model for easier access to teacher data
    teacher = relationship("Teacher", back_populates="courses")
    
class Teacher(Base):
    """Teacher model to store teacher information."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the Teacher
    name = Column(String, nullable=False)  # Required field for Teacher's name
    email = Column(String, nullable=False, unique=True)  # Required field for Teacher's email
    courses = relationship("Course", back_populates="teacher")  # Relationship for courses taught by this teacher

def upgrade():
    """Upgrade the database schema to include the teacher_id in courses."""
    # No specific migration commands here unless needed
    pass

def downgrade():
    """Downgrade the database schema by removing the teacher_id from courses."""
    # If needed, implement downgrade logic
    pass
```