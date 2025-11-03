```python
from app import db

class StudentCourses(db.Model):
    """Model to represent the many-to-many relationship between Students and Courses."""
    
    __tablename__ = 'student_courses'
    
    # Foreign key referencing the Student model
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    
    # Foreign key referencing the Course model
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    
    def __repr__(self):
        """Provide a string representation of the StudentCourses association."""
        return f"<StudentCourses(student_id={self.student_id}, course_id={self.course_id})>"
```