```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Adding teacher_id as Foreign Key

    # Establish relationship with Teacher model
    teacher = relationship('Teacher', back_populates='courses')

    def __repr__(self):
        return f"<Course id={self.id}, name={self.name}, teacher_id={self.teacher_id}>"
```
