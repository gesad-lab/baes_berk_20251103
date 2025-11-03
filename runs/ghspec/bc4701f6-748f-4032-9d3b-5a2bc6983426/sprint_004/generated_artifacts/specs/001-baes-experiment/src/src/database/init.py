```python
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

def initialize_database():
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)  # Create all tables including Enrollment

    # Ensure that all existing Student and Course data remain unaffected.
    # Logging to check schema creation
    print("Database initialized and schema created.")

# Add this method to your module or app initialization logic
def get_db_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_engine('sqlite:///app.db'))
    return SessionLocal()
```