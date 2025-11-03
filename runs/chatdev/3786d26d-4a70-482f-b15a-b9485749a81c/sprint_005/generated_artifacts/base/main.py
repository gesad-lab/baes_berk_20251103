'''
Migration script to create the Course table and ensure the existing Student table is intact.
'''
from sqlalchemy import create_engine, text  # Import text
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create the tables in the database
Base.metadata.create_all(engine)  # This will create both students and courses tables if they don't exist
# Create the association table
with engine.connect() as connection:
    connection.execute(text("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (course_id) REFERENCES courses (id)
    )
    """))  # Wrap the SQL string in text()
if __name__ == "__main__":
    print("Database migration completed.")