```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # Establish reverse relationship with Course model
    courses = relationship("Course", back_populates="teacher")
```