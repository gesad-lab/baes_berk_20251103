import sqlite3

def migrate():
    """Run migration to create the courses table in the database."""
    # Connect to the SQLite database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    try:
        # Create the courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                level TEXT NOT NULL
            );
        ''')
        print("Migration successful: courses table created.")
    except sqlite3.Error as e:
        # Log error during migration process
        print(f"Error in migration: {e}")
    finally:
        # Always commit changes and close the connection
        connection.commit()
        connection.close()

if __name__ == "__main__":
    migrate()