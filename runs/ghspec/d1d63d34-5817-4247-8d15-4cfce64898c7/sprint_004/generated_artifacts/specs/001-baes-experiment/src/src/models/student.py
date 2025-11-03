```python
# src/models/student.py
from typing import List
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import BaseModel  # assuming BaseModel imports from SQLAlchemy base

class Student(BaseModel):
    __tablename__ = 'student'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    courses: List[int] = relationship("Course", back_populates="students")  # assuming Course is defined elsewhere

    def assign_courses(self, course_ids: List[int]) -> List[str]:
        """Assign multiple courses to this student."""
        self.courses.extend(course_ids)  # extend the course list with new IDs
        # Here, you likely need to commit this change to the database

    def get_courses(self) -> List[int]:
        """Retrieve all courses associated with this student."""
        return self.courses

    def remove_course(self, course_id: int) -> None:
        """Remove a specific course from this student."""
        if course_id in self.courses:
            self.courses.remove(course_id)
            # Here, you likely need to commit this change to the database
        else:
            raise ValueError(f"Course ID {course_id} is not associated with this student.")
```