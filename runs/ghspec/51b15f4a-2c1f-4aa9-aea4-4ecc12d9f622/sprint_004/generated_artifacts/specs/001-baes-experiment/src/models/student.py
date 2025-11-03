```python
# models/student.py

from app import db

class Student(db.Model):
    """
    Student entity model that maps to the students table in the database.
    
    Attributes:
        id (int): Unique identifier for the student.
        name (str): The name of the student.
        enrollments (list): A list of Enrollment instances related to this student.
    """
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    # Relationship with Enrollment model
    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')

# Note: The Enrollment model needs to be defined in models/enrollment.py where it will reference this class.
```