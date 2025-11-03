```python
# src/models/teacher.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming that Base is defined for SQLAlchemy models

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Establish a one-to-many relationship with Course
    courses = relationship('Course', back_populates='teacher')

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```

**Note**: In this implementation, a one-to-many relationship is established between the `Teacher` model and the `Course` model through the `courses` attribute. The `back_populates` parameter is used to set up a bidirectional relationship, so ensure that the `Course` model is updated accordingly to include a reference back to the `Teacher`.