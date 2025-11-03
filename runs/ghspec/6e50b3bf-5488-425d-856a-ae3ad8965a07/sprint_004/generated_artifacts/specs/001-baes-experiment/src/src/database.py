```python
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey

# Initialize database and migration extensions
db = SQLAlchemy()
migrate = Migrate()

# Define the Student and Course models as needed
class Student(db.Model):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    # Other columns of the Student

class Course(db.Model):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    # Other columns of the Course

# New association table for Student and Course relationship
class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"

def initialize_app(app):
    """Initialize the database and migration with the Flask app context."""
    db.init_app(app)
    migrate.init_app(app, db)

# Migration command can be executed using Flask-Migrate commands in terminal
# To migrate changes: flask db migrate -m "Create Student_Course relationship table"
# Then upgrade to apply the migration: flask db upgrade
```