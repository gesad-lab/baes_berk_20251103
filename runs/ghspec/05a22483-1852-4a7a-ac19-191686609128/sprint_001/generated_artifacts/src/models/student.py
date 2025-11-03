from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    """ORM model representing the student entity with fields `id` and `name`."""
    
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self):
        """Converts the Student instance to a dictionary format for JSON responses."""
        return {
            'id': self.id,
            'name': self.name
        }