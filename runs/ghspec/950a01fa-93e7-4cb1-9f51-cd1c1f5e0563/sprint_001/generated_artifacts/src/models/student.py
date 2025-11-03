from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented primary key
    name = db.Column(db.String, nullable=False)    # Required field for student name

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(name={self.name})>"