import os
import sqlite3
from flask import current_app

DATABASE = 'students.db'

def get_db():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(os.path.join(current_app.root_path, DATABASE))
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def init_db():
    """Initializes the database schema for the application."""
    with current_app.app_context():
        db = get_db()
        cursor = db.cursor()

        # Create the Student table if it does not exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')
        db.commit()  # Commit changes
        db.close()  # Clean up, close the database connection

def init_app(app):
    """Initializes the application with database setup."""
    app.teardown_appcontext(close_db)  # Ensure DB connection is closed after requests
    init_db()  # Initialize the database on startup

def close_db(exception):
    """Closes the database connection."""
    db = getattr(current_app, '_database', None)
    if db is not None:
        db.close()