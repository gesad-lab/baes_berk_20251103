```python
# src/models.py

from your_app import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)  # Adding the teacher_id field

    # Relationships
    teacher = db.relationship('Teacher', backref='courses', foreign_keys=[teacher_id])

    def __repr__(self):
        return f'<Course {self.name}>'
```