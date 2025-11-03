```python
import sqlite3
from sqlite3 import Error

# Constants for error codes
E001 = "E001"  # Invalid email format
E002 = "E002"  # No updates made

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error creating connection: {e}")
    return conn

def update_student_email(student_id: int, new_email: str, conn: sqlite3.Connection):
    """
    Update a student's email in the database.
    
    :param student_id: ID of the student to update
    :param new_email: New email to set for the student
    :param conn: SQLite connection object
    :raises ValueError: If the email is invalid
    :return: Updated student's email on success, or an appropriate error message
    """
    # Validate email format
    if not validate_email(new_email):
        raise ValueError(f"{E001}: Invalid email format")

    # SQL command to update student email
    sql = ''' UPDATE students
              SET email = ?
              WHERE id = ? '''

    cur = conn.cursor()
    cur.execute(sql, (new_email, student_id))
    
    # Check if any update was performed
    if cur.rowcount == 0:
        raise ValueError(f"{E002}: No updates were made. Student ID might not exist.")

    conn.commit()
    return new_email

def validate_email(email: str) -> bool:
    """Check if the provided email is valid using basic validation."""
    # Basic validation criteria for email addresses
    return "@" in email and "." in email

# Sample usage
if __name__ == "__main__":
    database = "your_database.db"
    conn = create_connection(database)

    student_id = 1  # Example student ID
    new_email = "new.email@example.com"  # New email to be updated

    try:
        updated_email = update_student_email(student_id, new_email, conn)
        print(f"Student's email updated to: {updated_email}")
    except ValueError as e:
        print(f"Error: {e}")

    if conn:
        conn.close()
```