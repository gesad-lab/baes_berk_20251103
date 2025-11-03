```python
"""
Module: student_repository.py

This module provides the StudentRepository class, which implements CRUD 
operations for managing student records in a SQLite database. The operations
include creating, reading, updating, and deleting student records. 

The database schema is initialized to ensure a Students table is available.
"""

import sqlite3
from sqlite3 import Error
from typing import List, Dict, Any, Optional


class StudentRepository:
    """
    A repository for managing student records in a SQLite database.
    
    Responsibilities:
    - Create, read, update, and delete student records.
    - Manage database connection and initialization.
    """

    def __init__(self, db_file: str):
        """Initialize the repository with a database file."""
        self.connection = self.create_connection(db_file)
        self.initialize_schema()

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def initialize_schema(self) -> None:
        """Create the Students table if it doesn't exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except Error as e:
            print(f"Error initializing database schema: {e}")
            raise

    def create_student(self, name: str) -> Dict[str, Any]:
        """Create a new student record."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Students (name) VALUES (?)", (name,))
            self.connection.commit()
            return {"id": cursor.lastrowid, "name": name}
        except Error as e:
            print(f"Error creating student: {e}")
            raise

    def get_all_students(self) -> List[Dict[str, Any]]:
        """Retrieve all student records."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Students")
        rows = cursor.fetchall()
        return [{"id": row[0], "name": row[1]} for row in rows]

    def update_student(self, student_id: int, name: str) -> Optional[Dict[str, Any]]:
        """Update an existing student record."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Students SET name = ? WHERE id = ?", (name, student_id))
            if cursor.rowcount == 0:
                return None  # Student not found
            self.connection.commit()
            return {"id": student_id, "name": name}
        except Error as e:
            print(f"Error updating student: {e}")
            raise

    def delete_student(self, student_id: int) -> None:
        """Delete a student record."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Students WHERE id = ?", (student_id,))
            self.connection.commit()
        except Error as e:
            print(f"Error deleting student: {e}")
            raise

    def close(self) -> None:
        """Close the database connection."""
        if self.connection:
            self.connection.close()
```