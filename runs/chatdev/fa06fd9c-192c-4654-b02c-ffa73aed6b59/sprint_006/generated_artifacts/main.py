'''
Migration script to create the student_courses association table and the teachers table.
'''
from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, text  # Import text
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def migrate():
    with engine.connect() as connection:
        # Check if the association table already exists
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='student_courses';"))
        if not result.fetchone():
            # Create the association table if it does not exist
            connection.execute(text("""
            CREATE TABLE student_courses (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            )
            """))
        # Create Teacher table if it does not exist
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='teachers';"))
        if not result.fetchone():
            connection.execute(text("""
            CREATE TABLE teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """))
        # Add teacher_id column to courses table if it does not exist
        try:
            connection.execute(text("""
            ALTER TABLE courses ADD COLUMN teacher_id INTEGER;
            """))
        except Exception as e:
            print("Column 'teacher_id' may already exist or another error occurred:", e)
if __name__ == "__main__":
    migrate()