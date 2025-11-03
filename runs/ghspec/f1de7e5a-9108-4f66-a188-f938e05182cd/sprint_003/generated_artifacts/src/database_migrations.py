```python
# src/database_migrations.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the database connection
db = SQLAlchemy()

# Migration for creating the courses table
def create_courses_table():
    # Check if the courses table already exists to avoid duplication
    if not db.engine.dialect.has_table(db.engine, 'courses'):
        # Create courses table
        db.create_all()

    # Define the Courses model to create the table structure
    class Course(db.Model):
        __tablename__ = 'courses'
        
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String, nullable=False)
        level = db.Column(db.String, nullable=False)

    # Create the table in the database with the defined structure
    db.create_all()

if __name__ == "__main__":
    create_courses_table()
```