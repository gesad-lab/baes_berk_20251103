from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    
    # Adding email field to Student entity
    email = db.Column(db.String, nullable=False, unique=True)  # Unique email is required for each student

    def __init__(self, name: str, email: str):
        """Initialize a Student instance.

        Args:
            name (str): The name of the student.
            email (str): The email of the student, must be unique.
        """
        self.name = name
        self.email = email

    def __repr__(self):
        """String representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"