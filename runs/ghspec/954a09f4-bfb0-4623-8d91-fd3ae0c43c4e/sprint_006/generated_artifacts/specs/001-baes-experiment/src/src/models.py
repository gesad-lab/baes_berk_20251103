```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(db.String(100), nullable=False)
    
    # Relationship to link courses to this teacher
    courses = relationship('Course', back_populates='teacher')


class Course(db.Model):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(db.String(100), nullable=False)
    
    # New foreign key column to associate course with teacher
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Relationship to link this course to the teacher
    teacher = relationship('Teacher', back_populates='courses')
```