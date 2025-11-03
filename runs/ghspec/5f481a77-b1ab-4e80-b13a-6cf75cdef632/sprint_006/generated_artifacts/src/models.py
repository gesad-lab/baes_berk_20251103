```python
from src import db  # Assuming db is initialized in another module
from src.models import Teacher  # Import the Teacher model

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)
    
    # New relationship to associate Course with Teacher
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)  # Allow null if no teacher is assigned
    teacher = db.relationship('Teacher', backref='courses')  # Establish relationship

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level}, teacher_id={self.teacher_id})>"
```