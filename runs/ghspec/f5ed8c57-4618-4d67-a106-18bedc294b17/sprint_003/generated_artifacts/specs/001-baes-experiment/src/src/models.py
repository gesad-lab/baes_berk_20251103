```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class Course(Base):
    """Course model represents the courses offered in the application."""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    credits = Column(Float, nullable=False)

    # Optionally, a relationship, assuming a Course can have many Students (if needed)
    # students = relationship("Student", back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}', credits={self.credits})>"
```