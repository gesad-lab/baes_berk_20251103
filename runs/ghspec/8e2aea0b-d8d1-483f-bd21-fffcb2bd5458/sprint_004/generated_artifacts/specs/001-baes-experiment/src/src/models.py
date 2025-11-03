```python
from datetime import datetime
from src.models import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Course name
    description = db.Column(db.String(250))  # Optional course description
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of creation

    # Relationship to Student model (assuming it's defined in the same module)
    students = db.relationship('Student', backref='courses', lazy=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Course {self.name}>'
```