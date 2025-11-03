```python
# src/db.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, Migration
from src.models import Student, Course  # Importing existing models

# Initialize the database instance and migration
db = SQLAlchemy()
migrate = Migrate()

# Migration script for updating the database schema
def upgrade():
    """Function to run the migration."""
    # Add a new field to the Student model to store course IDs
    with db.engine.connect() as connection:
        # Implementing an 'enrollments' table to manage many-to-many relationships
        connection.execute("""
            CREATE TABLE course_enrollments (
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
            )
        """)

def downgrade():
    """Function to reverse the migration."""
    with db.engine.connect() as connection:
        # Drop the enrollments table if it exists
        connection.execute("""
            DROP TABLE IF EXISTS course_enrollments;
        """)

# Perform the upgrade when running the app
if __name__ == "__main__":
    with app.app_context():
        upgrade()
```
