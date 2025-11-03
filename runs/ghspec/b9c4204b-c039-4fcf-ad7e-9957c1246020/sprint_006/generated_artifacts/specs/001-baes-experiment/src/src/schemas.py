```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Add teacher_id column as FK

    # Establish relationship with Teacher entity
    teacher = relationship("Teacher", back_populates="courses")

# Migration SQL command to add teacher_id column and foreign key
def upgrade():
    # Add teacher_id column to courses table
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))
    
# The upgrade method encapsulates the migration for adding the column/foreign key.
```