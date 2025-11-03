import sqlite3
from contextlib import closing

DATABASE_PATH = 'student_management.db'

def migrate_add_email_field():
    """
    Adds the email field to the Student table in the database.
    
    This migration will add a new column 'email' of type VARCHAR(100) to the 
    existing Student table while ensuring that it does not affect existing records. 
    The email field will default to an empty string for existing rows.
    """
    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as connection:
            cursor = connection.cursor()
            # Check if the email column already exists
            cursor.execute("PRAGMA table_info(student);")
            columns = [column[1] for column in cursor.fetchall()]
            if 'email' not in columns:
                # Adding the email column with a default value of empty string
                cursor.execute("ALTER TABLE student ADD COLUMN email VARCHAR(100) NOT NULL DEFAULT '';")
                connection.commit()
                print("Migration successful: email field added.")
            else:
                print("Migration skipped: email field already exists.")
    except sqlite3.Error as e:
        # Log the error with context but do not expose sensitive information
        print(f"Migration failed: {e}")

# Run the migration function to apply the changes
if __name__ == "__main__":
    migrate_add_email_field()