"""
migrations.py

This module handles database migrations, including the addition of new fields 
to existing tables without data loss. It utilizes SQLAlchemy for ORM capabilities. 

### Migration Overview

- The 'students' table will be updated to include a new 'email' field which is 
  required for student records. This migration will ensure all existing student 
  data remains intact.

### API Changes
- The following API endpoints have been updated to reflect the changes made:
  - **POST /students**: Accepts a JSON payload that now includes:
    - `name`: String (required)
    - `email`: String (required)
  
  - **GET /students/{id}**: Returns student information including:
    - `name`: String
    - `email`: String

  - **GET /students**: Returns a list of all students, now including the 
    `email` field alongside `name`.
"""

from sqlalchemy import Column, String
from your_application.database import Base

class Migration:
    """
    Handles the migration of the Student entity to include the email field.
    """
    @staticmethod
    def add_email_field_to_students_table():
        """
        Adds the email field to the existing students table.

        This function will check if the email column exists before attempting to
        add it, preventing errors during the migration process.
        """
        # Check if the column 'email' already exists to avoid duplication
        if not Migration.column_exists('students', 'email'):
            # Perform the migration to add 'email' to the student table
            with Base.metadata.bind.begin() as connection:
                connection.execute('ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL')

    @staticmethod
    def column_exists(table_name, column_name):
        """
        Checks if a column exists in a given table.

        Args:
            table_name (str): The name of the table in the database.
            column_name (str): The name of the column to check.

        Returns:
            bool: True if the column exists, False otherwise.
        """
        inspector = inspect(Base.metadata.bind)
        columns = [col['name'] for col in inspector.get_columns(table_name)]
        return column_name in columns
