```python
from your_app import db  # replace with actual import path

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # New foreign key
    # Other existing fields...

    def __init__(self, teacher_id=None, **kwargs):
        """
        Initialize a Course instance.
        
        :param teacher_id: Foreign key reference to Teacher model.
        :param kwargs: Other attributes for the Course model.
        """
        self.teacher_id = teacher_id
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Course id={self.id}, teacher_id={self.teacher_id}>'
```