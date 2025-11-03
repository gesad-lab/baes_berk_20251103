```python
from src.database import db

class StudentCourse(db.Model):
    """Model for the association between students and courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    
    def __repr__(self):
        return f"<StudentCourse student_id={self.student_id} course_id={self.course_id}>"
```