```python
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def migrate_database():
    """Perform database migrations including adding an email column to the students table."""
    # Connect to the SQLite database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # SQL command to add the email column if it doesn't exist
    try:
        cursor.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT '';")
        connection.commit()  # Commit the changes to the database
    except sqlite3.OperationalError as e:
        # Handle the case where the column already exists
        if "duplicate column name: email" not in str(e):
            # Log an error message if it's not a duplicate column error
            print(f"Migration failed: {e}")
    finally:
        cursor.close()
        connection.close()

# Call the migration function when this script is executed
if __name__ == "__main__":
    migrate_database()
```