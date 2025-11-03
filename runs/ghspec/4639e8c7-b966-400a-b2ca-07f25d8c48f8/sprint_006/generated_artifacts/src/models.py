```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base  # Assuming Base is defined as part of the SQLAlchemy setup

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Optional foreign key to Teacher
    
    teacher = relationship("Teacher")  # Establish relationship with the Teacher model

    def __repr__(self):
        return f"<Course(title={self.title}, teacher_id={self.teacher_id})>"
```