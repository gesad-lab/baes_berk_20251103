```python
import os
import sqlite3
from typing import List, Dict

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///students.db")

class StudentDatabase:
    def __init__(self):
        """Initialize the StudentDatabase and create the table if it doesn't exist."""
        self.connection = sqlite3.connect(self._get_database_uri())
        self._create_table()

    def _get_database_uri(self) -> str:
        """Extracts and returns the database URI. Supports SQLite in a controlled environment."""
        uri = DATABASE_URI.replace("sqlite:///", "")  # SQLite uses file path without the prefix
        return uri

    def _create_table(self):
        """Creates the 'students' table if it doesn't already exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            ''')

    def add_student(self, name: str) -> int:
        """Adds a new student to the database.

        Args:
            name (str): The name of the student.

        Returns:
            int: The ID of the newly created student.
        """
        with self.connection:
            cursor = self.connection.execute('''
                INSERT INTO students (name) VALUES (?)
            ''', (name,))
            return cursor.lastrowid

    def get_all_students(self) -> List[Dict[str, str]]:
        """Retrieves all students from the database.

        Returns:
            List[Dict[str, str]]: A list of student records with their IDs and names.
        """
        cursor = self.connection.execute('SELECT id, name FROM students')
        return [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]

    def close(self):
        """Closes the database connection."""
        self.connection.close()
```
