from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    """Represents a Student entity with a name."""

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each student
    name = db.Column(db.String, nullable=False)    # Name of the student, required field

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student id={self.id} name={self.name}>"

    def to_dict(self):
        """
        Convert the Student instance to a dictionary format.

        Returns:
            dict: A dictionary representation of the Student.
        """
        return {
            "id": self.id,
            "name": self.name
        }