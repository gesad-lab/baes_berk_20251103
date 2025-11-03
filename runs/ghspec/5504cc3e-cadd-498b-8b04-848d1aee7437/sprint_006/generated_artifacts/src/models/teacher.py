```python
# src/models/teacher.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src import db

class Teacher(db.Model):
    """Model representing a teacher."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Establishing a reverse relationship to courses
    courses = relationship('Course', back_populates='teacher')


# src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src import db

class Course(db.Model):
    """Model representing a course."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    # Adding a foreign key that links to the Teacher model
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    # Establishing a relationship to Teacher
    teacher = relationship('Teacher', back_populates='courses')
```