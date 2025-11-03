'''
Migration script to add email field to Student entity and create Course entity.
'''
from sqlalchemy import Column, String, Integer, create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from database import init_db  # Importing init_db to ensure database initialization
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)  # Changed to nullable initially
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
def upgrade():
    '''
    Adds the email column to the existing Student table and creates the Course table.
    '''
    with engine.connect() as connection:
        # Check if the students table exists before altering
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='students';"))
        if result.fetchone() is not None:
            # Add email column as nullable first
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT'))  # Wrapped in text()
            # Update existing records with a default value to comply with the required field
            connection.execute(text('UPDATE students SET email = "default@example.com" WHERE email IS NULL'))  # Wrapped in text()
        # Create the courses table
        connection.execute(text('CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, name TEXT NOT NULL, level TEXT NOT NULL)'))
        # Create the association table for the many-to-many relationship
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS student_courses (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
            )
        '''))
def downgrade():
    '''
    Removes the email column from the Student table if needed.
    '''
    with engine.connect() as connection:
        connection.execute(text('ALTER TABLE students DROP COLUMN email'))  # Wrapped in text()
if __name__ == "__main__":
    init_db()  # Ensure the database and tables are created first
    upgrade()  # Then run the upgrade to add the email field and create the Course table