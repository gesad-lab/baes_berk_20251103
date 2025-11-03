from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import Course

def upgrade():
    """
    Migration script to add `teacher_id` foreign key to `courses` table.
    This establishes a relationship between Courses and Teachers, 
    allowing each Course to be associated with one Teacher.
    """

    # Create a database engine for SQLite
    engine = create_engine('sqlite:///database.db')  # Ensure the path matches existing db
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Open a connection to the database
        with engine.connect() as connection:
            # Alter the 'courses' table to add the 'teacher_id' foreign key
            connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);')

        # Commit the changes to the session to ensure they are saved
        session.commit()

    except Exception as e:
        # Rollback session in case of an error
        session.rollback()
        print(f"Error occurred during migration: {e}")
    finally:
        # Close the session to avoid resource leaks
        session.close()