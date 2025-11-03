from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

# Database connection setup
DATABASE_URL = "sqlite:///./test.db"  # Placeholder for the database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def add_email_field():
    """Migration script to add the email column to the students table."""
    try:
        # This assumes the engine has already been defined
        # Ensure the Student table exists
        Base.metadata.create_all(bind=engine)

        # Start a new session
        db = SessionLocal()
        
        # Add the email column to the students table
        with db.begin():
            # Here we're assuming we're using Alembic or similar for schema migrations
            sql = '''
            ALTER TABLE students
            ADD COLUMN email VARCHAR NOT NULL;  -- Required new email field
            '''
            db.execute(sql)

        print("Email column added to students table successfully.")

    except Exception as e:
        # Log the exception for debugging
        print(f"Error occurred while adding email column: {e}")
    finally:
        # Clean up session to avoid resource leaks
        db.close()

if __name__ == "__main__":
    add_email_field()  # Run the migration script if executed directly