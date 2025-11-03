```python
import sqlite3
from sqlite3 import Connection, Cursor

# Migration script to add the Course table to the database
def migrate_add_course_table(connection: Connection) -> None:
    """Create the Course table in the database if it doesn't exist.

    Args:
        connection (Connection): The SQLite database connection.
    
    Raises:
        sqlite3.Error: If there is an error during the migration process.
    """
    try:
        with connection:
            # Create Course table with the required fields
            connection.execute("""
                CREATE TABLE IF NOT EXISTS Course (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    level TEXT NOT NULL
                );
            """)
    except sqlite3.Error as e:
        print(f"Error occurred while migrating: {e}")
        raise

# Usage of the migration script
if __name__ == "__main__":
    db_connection = sqlite3.connect("database.db")  # Adjust the database path as needed
    migrate_add_course_table(db_connection)
    db_connection.close()
```