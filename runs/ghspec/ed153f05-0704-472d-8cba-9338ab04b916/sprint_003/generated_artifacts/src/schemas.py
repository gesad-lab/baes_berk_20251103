```python
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Course(db.Model):
    """Course model representing the courses available in the system."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Required field for the name of the course
    level = db.Column(db.String, nullable=False)  # Required field for the level of the course

class CourseSchema(SQLAlchemyAutoSchema):
    """Schema for serializing and validating Course instances."""
    
    class Meta:
        model = Course
        fields = ("id", "name", "level")

# After defining the Course table, ensure to make a migration
# Run the following commands to create and apply the migration:
# flask db migrate -m "Add Course table"
# flask db upgrade
```