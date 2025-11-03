```python
# src/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Course(db.Model):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Adding teacher_id field

    # Defining the relationship with Teacher
    teacher = relationship("Teacher", backref="courses", lazy='joined')

    def __repr__(self):
        return f"<Course (id={self.id}, name={self.name}, level={self.level}, teacher_id={self.teacher_id})>"
```