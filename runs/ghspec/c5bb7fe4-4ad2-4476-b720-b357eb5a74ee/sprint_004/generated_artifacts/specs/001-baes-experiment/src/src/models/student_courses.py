```python
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class StudentCourses(db.Model):
    """Model representing the association between Students and Courses."""
    
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourses(student_id={self.student_id}, course_id={self.course_id})>"
```