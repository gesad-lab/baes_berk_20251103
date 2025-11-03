```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for declarative model definitions
Base = declarative_base()

class Student(Base):
    """Model representing a student entity."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class StudentDataAccess:
    """Data Access Layer for managing student records in the database."""

    def __init__(self, database_url: str):
        """Initialize the StudentDataAccess with a database URL."""
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_student_table(self):
        """Create the student table in the database if it doesn't exist."""
        try:
            # Create all tables in the engine. This will create the students table if it doesn't exist.
            Base.metadata.create_all(self.engine)
            print("Student table created successfully.")
        except Exception as e:
            # Log the error with context
            print(f"Error creating student table: {e}")

# Example initialization (to be called at startup)
# dal = StudentDataAccess("sqlite:///students.db")
# dal.create_student_table()
```