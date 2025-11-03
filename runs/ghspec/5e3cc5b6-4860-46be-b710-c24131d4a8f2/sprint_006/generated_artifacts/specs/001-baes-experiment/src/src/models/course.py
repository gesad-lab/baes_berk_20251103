```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Added teacher_id field

    teacher = relationship("Teacher", back_populates="courses")  # Establishing the relationship with Teacher

# It's assumed that the Teacher model has a corresponding back-populates attribute
# for the sake of establishing a bidirectional relationship:
# In the Teacher model, it should look like this:
# courses = relationship("Course", back_populates="teacher")
```