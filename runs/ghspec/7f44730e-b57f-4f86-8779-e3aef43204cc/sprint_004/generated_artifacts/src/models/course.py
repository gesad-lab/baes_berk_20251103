```python
# src/models/course.py
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # New relationship declaration for many-to-many with Student
    students = relationship("StudentCourse", back_populates="course")
```