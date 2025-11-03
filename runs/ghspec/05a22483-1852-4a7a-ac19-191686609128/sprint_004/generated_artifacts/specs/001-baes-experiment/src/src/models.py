```python
from your_app import db  # Importing the db object from the application
from your_app.models import Student, Course  # Ensure we can reference existing Student and Course models

class Enrollment(db.Model):
    """Represents the join table between Students and Courses."""
    
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Enrollment table
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)  # Foreign key referencing Student
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)  # Foreign key referencing Course

    student = db.relationship('Student', backref='enrollments')  # Relationship with Student
    course = db.relationship('Course', backref='enrollments')  # Relationship with Course

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"  # String representation for debugging
```