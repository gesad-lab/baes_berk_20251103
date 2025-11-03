```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def init_db(app):
    """Initializes the database with the given Flask app."""
    db.init_app(app)

    # Create all tables defined by the models
    with app.app_context():
        db.create_all()

# Define the StudentCourse join model for the relationship between Students and Courses
class StudentCourse(db.Model):
    """Model for representing the many-to-many relationship between Students and Courses."""
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f'<StudentCourse student_id={self.student_id} course_id={self.course_id}>'
```