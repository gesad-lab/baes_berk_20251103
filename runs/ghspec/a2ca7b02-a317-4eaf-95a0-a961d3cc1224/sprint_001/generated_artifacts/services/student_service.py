```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base, Student  # Assuming Base is defined in models/student.py

DATABASE_URL = "sqlite:///./students.db"

# Initialize SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating the schema if it does not exist.
    This function should be called on application startup.
    """
    try:
        # Create the database schema if it doesn't exist
        Base.metadata.create_all(bind=engine)
        print("Database schema created or already exists.")
    except Exception as e:
        # Log the error (Consider using a logging framework in a real application)
        print(f"Failed to create database schema: {e}")

def get_db():
    """
    Provides a database session for use in requests.
    Yields a session and ensures proper handling.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Additional service functions for creating and retrieving students can be implemented here

def create_student(db: Session, name: str):
    """
    Create a new student in the database.

    Parameters:
    - db (Session): The database session.
    - name (str): The name of the student.
    
    Returns:
    - Student: The created student object.
    """
    db_student = Student(name=name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    """
    Retrieve all students from the database.

    Parameters:
    - db (Session): The database session.

    Returns:
    - list: A list of student objects.
    """
    return db.query(Student).all()

# Call the init_db function to ensure the schema is created on application startup
init_db()
```