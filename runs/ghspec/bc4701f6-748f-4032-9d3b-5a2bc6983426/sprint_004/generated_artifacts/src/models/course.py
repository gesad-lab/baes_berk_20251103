```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    # Existing fields (assuming they are defined)...
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String)

    # Establish relationship with Enrollment
    enrollments = relationship("Enrollment", back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```