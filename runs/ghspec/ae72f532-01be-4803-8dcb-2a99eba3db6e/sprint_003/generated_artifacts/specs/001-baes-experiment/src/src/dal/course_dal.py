```python
# src/dal/course_dal.py

import sqlite3
from typing import List, Optional
from src.models.course import Course  # Assuming Course model is defined in models/course.py
from src.config import DATABASE_PATH  # Path to the SQLite database

class CourseDAL:
    """Data Access Layer for Course entity to handle database operations."""

    def __init__(self, db_path: str = DATABASE_PATH):
        """Initialize the data access layer with the database path."""
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row  # Enable accessing rows by column name

    def create_course(self, name: str, level: str) -> Course:
        """Create a new course in the database.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Course: The created Course object containing id, name, and level.
        """
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO courses (name, level) VALUES (?, ?)", (name, level))
            course_id = cursor.lastrowid  # Get the id of the newly created course
            return Course(id=course_id, name=name, level=level)

    def get_all_courses(self) -> List[Course]:
        """Retrieve all courses from the database.

        Returns:
            List[Course]: A list of Course objects.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        return [Course(id=row['id'], name=row['name'], level=row['level']) for row in courses]

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage:
# dal = CourseDAL()
# new_course = dal.create_course("Mathematics", "Undergraduate")
# print(new_course)
# all_courses = dal.get_all_courses()
# print(all_courses)
# dal.close()
```