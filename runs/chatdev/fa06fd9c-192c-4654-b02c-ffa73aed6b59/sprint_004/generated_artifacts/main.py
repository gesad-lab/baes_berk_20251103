'''
Migration script to create the student_courses association table.
'''
from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, text  # Import text
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def migrate():
    with engine.connect() as connection:
        # Check if the association table already exists
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='student_courses';"))  # Wrapped in text()
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
            """))  # Wrapped in text()
        else:
            print("The student_courses table already exists. No changes made.")
if __name__ == "__main__":
    migrate()