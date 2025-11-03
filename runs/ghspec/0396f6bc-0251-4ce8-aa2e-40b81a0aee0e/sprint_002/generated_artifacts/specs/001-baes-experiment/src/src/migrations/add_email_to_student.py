from sqlalchemy import Column, String, Integer, create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (UniqueConstraint('email', name='uq_email'),)  # Ensure email is unique
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New Email field added

# Migration script
def add_email_to_student(engine):
    with engine.connect() as connection:
        # Alter the table to add the email column
        connection.execute("""
            ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL;
        """)
        # Ensure uniqueness on the email column (if not already handled by constraints)
        connection.execute("""
            CREATE UNIQUE INDEX uq_email ON students(email);
        """)

# Database initialization
def initialize_database():
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)  # Create tables
    add_email_to_student(engine)  # Run migration to add email field

if __name__ == "__main__":
    initialize_database()  # Initialize the database with the new schema