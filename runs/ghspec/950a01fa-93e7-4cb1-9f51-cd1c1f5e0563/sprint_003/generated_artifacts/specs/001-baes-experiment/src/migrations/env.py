```python
# migrations/env.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update with your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Course(db.Model):
    """Course model representing the courses in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Course name, required
    level = db.Column(db.String, nullable=False)  # Course level, required

def create_course_table():
    """Create the Course table in the database if it does not exist."""
    with app.app_context():  # Ensure we have application context
        db.create_all()  # Create all tables, including the Course table

if __name__ == '__main__':
    try:
        create_course_table()  # Call the function to create the Course table
        print("Migration completed: Course table created successfully.")
    except Exception as e:
        print(f"Migration failed: {e}")  # Print error if migration fails
```
