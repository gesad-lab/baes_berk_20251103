```python
from app import db

class StudentCourse(db.Model):
    """Model to represent the relationship between Students and Courses."""
    
    __tablename__ = 'student_courses'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    # Establishing relationships for easier querying
    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrolled_students', lazy=True))
```