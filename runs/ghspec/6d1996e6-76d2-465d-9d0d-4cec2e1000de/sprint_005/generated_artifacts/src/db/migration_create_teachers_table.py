```python
import sqlite3
from sqlite3 import Connection, Error

def create_connection(db_file: str) -> Connection:
    """Create a database connection to the SQLite database specified by db_file."""
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(f"Error creating connection: {e}")  # Log connection error
        return None

def create_teachers_table(connection: Connection) -> None:
    """Create the teachers table in the database."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()  # Commit changes to the database
    except Error as e:
        print(f"Error creating teachers table: {e}")  # Log table creation error
        connection.rollback()  # Rollback in case of an error

def main() -> None:
    """Main function to run the migration."""
    database = "path_to_your_database.db"  # Specify your database path
    connection = create_connection(database)
    
    if connection:
        create_teachers_table(connection)
        connection.close()  # Close the connection after the migration

if __name__ == '__main__':
    main()
```