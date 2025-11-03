```python
# src/db/health_check.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file: str):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def check_database_health(conn):
    """Check the health of the database by executing a simple query.
    
    Args:
        conn: The database connection object.
        
    Returns:
        bool: True if the database is healthy, False otherwise.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")  # Simple query to check if the database connection is active
        cursor.fetchone()
        return True
    except Error as e:
        print(f"Database health check failed: {e}")
        return False

def main(database: str):
    """Main function to perform the health check on the database."""
    conn = create_connection(database)
    if conn:
        is_healthy = check_database_health(conn)
        if is_healthy:
            print("Database is healthy.")
        else:
            print("Database is not healthy.")
        conn.close()
    else:
        print("Failed to create database connection.")

if __name__ == "__main__":
    database_path = "path/to/your/database.db"  # Change this to your database path
    main(database_path)
```