```python
# src/db/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")  # Example with SQLite
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Migration function to create student_courses table
def migrate():
    """Create the student_courses table linking students and courses."""
    with engine.connect() as connection:
        # SQL statement to create the junction table
        create_table_sql = text("""
        CREATE TABLE IF NOT EXISTS student_courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
            UNIQUE (student_id, course_id)  -- Prevent duplicate enrollments
        );
        """)
        connection.execute(create_table_sql)
        connection.commit()

# Run migrations
if __name__ == "__main__":
    migrate()
```