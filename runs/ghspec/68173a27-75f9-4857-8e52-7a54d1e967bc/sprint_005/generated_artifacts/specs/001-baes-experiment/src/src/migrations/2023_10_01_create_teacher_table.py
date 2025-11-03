```python
from sqlalchemy import Column, Integer, String, UniqueConstraint
from src.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each teacher
    name = Column(String, nullable=False)  # Required field for the teacher's name
    email = Column(String, nullable=False, unique=True)  # Required and unique field for the teacher's email

    __table_args__ = (
        UniqueConstraint('email', name='uq_teacher_email'),  # Ensures email uniqueness
    )
```