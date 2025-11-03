```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    """Model for the Course entity."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship

    # Relationship with Teacher
    teacher = relationship('Teacher', back_populates='courses')

    def assign_teacher(self, teacher_id):
        """Assigns a teacher to this course by updating the teacher_id."""
        self.teacher_id = teacher_id

    def get_course_details(self):
        """Returns course details including the assigned teacher's name and email if available."""
        teacher_info = {
            'name': self.teacher.name if self.teacher else None,
            'email': self.teacher.email if self.teacher else None
        }
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'teacher': teacher_info
        }
```