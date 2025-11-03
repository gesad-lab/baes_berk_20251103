```python
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Initialize the database
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    courses = relationship('Course', secondary='student_course', back_populates='students')

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    students = relationship('Student', secondary='student_course', back_populates='courses')

class StudentCourse(db.Model):
    """Junction table to establish many-to-many relationship between Student and Course."""
    __tablename__ = 'student_course'
    
    student_id = db.Column(db.Integer, ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, ForeignKey('courses.id'), primary_key=True)

    # Optionally, we can define relationships here for ease of accessing related entities
    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

def upgrade():
    """Upgrade the database schema to include the StudentCourse relationship."""
    # Create the StudentCourse table
    db.create_all()  # Create necessary tables if they don't exist

def downgrade():
    """Downgrade the database schema by removing the StudentCourse table."""
    db.drop_all()  # Drop tables in reverse order if necessary
```