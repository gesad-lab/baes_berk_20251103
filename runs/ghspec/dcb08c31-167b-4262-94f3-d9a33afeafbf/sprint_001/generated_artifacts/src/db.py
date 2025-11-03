import sqlite3

DATABASE_NAME = 'students.db'

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        print(f'Successfully connected to the database: {DATABASE_NAME}')
    except sqlite3.Error as e:
        print(f'Error connecting to database: {e}')
    return conn

def create_students_table(conn):
    """Create the students table in the database if it does not exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        print('Students table created successfully.')
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error creating students table: {e}')

def initialize_database():
    """Initialize the database by creating the necessary schema."""
    conn = create_connection()
    if conn:
        create_students_table(conn)
        conn.close()

if __name__ == '__main__':
    initialize_database()