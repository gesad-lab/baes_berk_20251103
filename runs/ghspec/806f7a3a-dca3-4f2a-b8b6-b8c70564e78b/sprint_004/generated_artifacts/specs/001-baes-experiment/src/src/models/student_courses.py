```python
from app import db

class StudentCourses(db.Model):
    """Mapping table for the many-to-many relationship between Student and Course."""
    
    __tablename__ = 'student_courses'

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

    # Relationships for ORM
    student = db.relationship('Student', back_populates='courses')
    course = db.relationship('Course', back_populates='students')

    def __repr__(self):
        """Return a string representation of the StudentCourses record."""
        return f"<StudentCourses(student_id={self.student_id}, course_id={self.course_id})>"
```