```python
from datetime import datetime
from src.database import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    courses = db.relationship('Course', secondary='student_courses', back_populates='students')

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    students = db.relationship('Student', secondary='student_courses', back_populates='courses')

class StudentCourses(db.Model):
    __tablename__ = 'student_courses'

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Establishing relationships for ORM compatibility
    student = db.relationship(Student, backref='enrollment')
    course = db.relationship(Course, backref='enrollment')

    def __repr__(self):
        return f"<StudentCourses(student_id={self.student_id}, course_id={self.course_id}, enrolled_at={self.enrolled_at})>"
```