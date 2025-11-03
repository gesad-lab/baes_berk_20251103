```python
from flask_sqlalchemy import SQLAlchemy

# Initialize database
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # Adding teacher_id as a foreign key referencing Teacher entity
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)

    def __repr__(self):
        return f'<Course {self.name}>'

    @staticmethod
    def validate_teacher_id(teacher_id):
        """ Validate that the teacher_id points to a valid Teacher entry. """
        if teacher_id:
            from models import Teacher  # Import here to avoid circular dependency
            teacher = Teacher.query.get(teacher_id)
            if teacher is None:
                raise ValueError(f"Invalid teacher_id: {teacher_id}, corresponding Teacher not found.")

    def assign_teacher(self, teacher_id):
        """ Assign a teacher to the course. """
        self.validate_teacher_id(teacher_id)
        self.teacher_id = teacher_id

    @property
    def teacher(self):
        """ Get the associated teacher for the course. """
        from models import Teacher  # Import here to avoid circular dependency
        return Teacher.query.get(self.teacher_id)
```