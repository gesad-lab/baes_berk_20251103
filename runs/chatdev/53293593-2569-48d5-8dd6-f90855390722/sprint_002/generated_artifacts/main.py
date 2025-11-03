'''
Handles database migrations to add the email field to the Student entity.
'''
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import MetaData
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
# Create a new migration
def migrate():
    metadata = MetaData()
    metadata.reflect(bind=engine)  # Corrected line
    if 'students' in metadata.tables:
        with engine.connect() as connection:
            # Step 1: Add the email column as nullable
            connection.execute('ALTER TABLE students ADD COLUMN email TEXT')
            # Step 2: Update existing records with a default value
            connection.execute('UPDATE students SET email = "" WHERE email IS NULL')
            # Step 3: Alter the column to be NOT NULL (if necessary)
            connection.execute('ALTER TABLE students RENAME TO students_old')
            connection.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)')
            connection.execute('INSERT INTO students (id, name, email) SELECT id, name, email FROM students_old')
            connection.execute('DROP TABLE students_old')
if __name__ == "__main__":
    migrate()