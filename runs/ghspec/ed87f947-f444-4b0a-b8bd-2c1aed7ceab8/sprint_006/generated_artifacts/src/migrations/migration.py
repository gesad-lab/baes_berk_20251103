```python
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming Base is imported from the database module

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # New field to associate a teacher with a course
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    # Relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Back reference to access courses associated with this teacher
    courses = relationship("Course", back_populates="teacher")

def upgrade():
    # Create migration steps for adding 'teacher_id' to the 'courses' table.
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    # Steps to reverse the migration
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```