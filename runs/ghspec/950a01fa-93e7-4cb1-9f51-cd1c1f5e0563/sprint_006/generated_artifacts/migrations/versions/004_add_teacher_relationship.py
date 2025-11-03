```python
# migrations/versions/004_add_teacher_relationship.py

from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define a base class for declarative model definitions
Base = declarative_base()

# Assuming the existing Course and Teacher models are defined in your models module
# Example definitions for context, adjust as per your actual model definitions
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New Foreign Key relationship

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    courses = relationship("Course", back_populates="teacher")

# Migration script
def upgrade():
    """Add teacher_id column to the courses table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_courses', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    """Remove teacher_id column from the courses table."""
    op.drop_constraint('fk_teacher_courses', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')

# To apply the migration, ensure that the database URL is set in your environment
if __name__ == "__main__":
    DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
```
