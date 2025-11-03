```python
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Teacher(Base):
    """Model for the Teacher entity."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String, nullable=False)

    # New relationship to the Course entity
    courses = relationship('Course', back_populates='teacher')

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```