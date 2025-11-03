from sqlalchemy import Column, Integer, String
from your_app import db  # Adjust import based on your app structure


class Course(db.Model):
    """Represents a course in the system."""
    
    __tablename__ = 'courses'  # Define the table name

    id = Column(Integer, primary_key=True, autoincrement=True)  # Course ID, auto-increment
    name = Column(String, nullable=False)  # Course name, cannot be null
    level = Column(String, nullable=False)  # Course level, cannot be null

    def __repr__(self):
        """Return a string representation of the course."""
        return f'<Course id={self.id} name={self.name} level={self.level}>'