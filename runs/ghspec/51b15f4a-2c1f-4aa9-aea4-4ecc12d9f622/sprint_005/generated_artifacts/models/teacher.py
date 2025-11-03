```python
# models/teacher.py

from app import db

class Teacher(db.Model):
    """
    Teacher entity model that maps to the teachers table in the database.
    
    Attributes:
        id (int): Unique identifier for the teacher.
        name (str): The name of the teacher.
        email (str): The email address of the teacher.
    """
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name}>'
```