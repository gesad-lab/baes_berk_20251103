from app import db

class Course(db.Model):
    """Represents a Course that is taught by a Teacher."""
    
    __tablename__ = 'courses'  # Define the table name in the database
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key for Course
    name = db.Column(db.String(100), nullable=False)  # Name of the Course
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)  # Foreign key for Teacher
    
    # Establish relationship with the Teacher model
    teacher = db.relationship("Teacher", back_populates="courses")  

    def __repr__(self):
        """Provide a formatted string representation of the Course."""
        return f'<Course {self.name}, Teacher ID: {self.teacher_id}>'