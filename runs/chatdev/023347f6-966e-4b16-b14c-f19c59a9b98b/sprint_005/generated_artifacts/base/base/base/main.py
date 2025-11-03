'''
Migration script to add email column to the students table.
'''
from sqlalchemy import create_engine, Column, String, Integer  # Added Integer import
from sqlalchemy.orm import sessionmaker, declarative_base  # Changed import for declarative_base
from sqlalchemy import inspect
Base = declarative_base()
DATABASE_URL = "sqlite:///./students.db"
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)  # New email column
def upgrade():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    inspector = inspect(engine)
    # Check if the 'students' table exists
    if 'students' in inspector.get_table_names():
        # Add the email column if it doesn't exist
        with connection.begin():
            connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL')
    else:
        Base.metadata.create_all(engine)  # Create the table if it doesn't exist
if __name__ == "__main__":
    upgrade()