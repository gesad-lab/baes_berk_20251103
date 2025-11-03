```python
from app import db
from sqlalchemy import Column, Integer, ForeignKey

class StudentCourse(db.Model):
    """Model representing the association between a Student and a Course."""
    
    __tablename__ = 'student_course'
    
    # ForeignKey referencing the students table
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    # ForeignKey referencing the courses table
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f'<StudentCourse student_id={self.student_id} course_id={self.course_id}>'
```