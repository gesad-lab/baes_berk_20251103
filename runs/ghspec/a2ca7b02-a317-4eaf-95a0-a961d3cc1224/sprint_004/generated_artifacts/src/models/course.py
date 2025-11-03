```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

# Association table to facilitate many-to-many relationship between Students and Courses
association_table = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    VALID_LEVELS = {"Beginner", "Intermediate", "Advanced"}

    @validates('name')
    def validate_name(self, key, value):
        # Validation logic for course name
        return value

    # Relationship to represent students enrolled in the course
    students = relationship("Student", secondary=association_table, back_populates="courses")
```