import sqlite3

def migrate():
    """Migrate the database schema to include the email field in the StudentResponse model."""
    connection = sqlite3.connect('students.db')  # Connect to the SQLite database
    cursor = connection.cursor()

    # Check if the 'students' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';")
    if cursor.fetchone() is not None:
        # Alter the 'students' table to add an email column
        cursor.execute("ALTER TABLE students ADD COLUMN email TEXT;")
    else:
        # If the table does not exist, raise an error
        raise Exception("Students table does not exist!")

    connection.commit()  # Commit the changes
    connection.close()  # Close the database connection

if __name__ == "__main__":
    try:
        migrate()
        print("Database migration successful: 'email' column added to 'students' table.")
    except Exception as e:
        print(f"Database migration failed: {e}")