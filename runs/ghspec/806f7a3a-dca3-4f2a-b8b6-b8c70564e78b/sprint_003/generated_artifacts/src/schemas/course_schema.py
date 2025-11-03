```python
from app import db

# Define the Course model
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each course
    name = db.Column(db.String(100), nullable=False)  # Name of the course
    level = db.Column(db.String(50), nullable=False)  # Level of the course

    def __repr__(self):
        return f'<Course {self.name}>'
        

# Migration script for creating the courses table
def upgrade():
    # Create the courses table
    db.create_all()

def downgrade():
    # Drop the courses table if it exists
    db.drop_all()
```