import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error '{e}' occurred while connecting to the database.")

    return conn

def migrate_add_email_to_students(conn):
    """Add an email field to the students table while preserving existing data."""
    try:
        cursor = conn.cursor()
        
        # Check if the 'email' column already exists
        cursor.execute("PRAGMA table_info(students);")
        columns = [column[1] for column in cursor.fetchall()]
        if 'email' not in columns:
            # Add 'email' column to the 'students' table
            cursor.execute("ALTER TABLE students ADD COLUMN email TEXT;")
            print("Migration: 'email' column added to 'students' table.")
        else:
            print("Migration: 'email' column already exists in 'students' table.")
        
        conn.commit()
    except Error as e:
        print(f"Error '{e}' occurred during migration.")
    finally:
        cursor.close()

def main():
    database = "student_entity.db"  # Path to the SQLite database

    # Create a database connection
    conn = create_connection(database)

    if conn:
        migrate_add_email_to_students(conn)
        conn.close()
    else:
        print("Migration failed. No connection to the database.")

if __name__ == "__main__":
    main()