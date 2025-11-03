```python
from app import db
from sqlalchemy import Column, Integer, ForeignKey

class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```