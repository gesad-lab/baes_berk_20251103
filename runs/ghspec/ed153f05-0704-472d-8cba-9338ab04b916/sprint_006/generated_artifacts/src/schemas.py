```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database import db, ma
from src.models import Course  # Import existing Course model

# Define the Course model (if not present)
class Course(db.Model):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field for relationship

    # Establishing relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")


# Update the CourseSchema to include the teacher_id field
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_fk = True  # Include foreign key fields in the schema

# Provide a migration function to add the teacher_id column to the courses table
def migrate():
    """Function to handle database migration for courses table."""
    with db.session.begin():
        db.engine.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id)')

# Call the migration function
migrate()
```