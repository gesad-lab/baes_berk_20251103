```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Teacher(Base):
    """This class defines the Teacher model representing teacher data in the database."""

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each teacher
    name = Column(String, index=True)  # Name of the teacher
    email = Column(String, unique=True, index=True)  # Email of the teacher
    courses = relationship("Course", back_populates="teacher")  # Relationship to courses taught by this teacher

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```