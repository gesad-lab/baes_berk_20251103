```python
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

# Define the base for the models
Base = declarative_base()

# Define Teacher model to represent the teacher table
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, Sequence('teacher_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Connect to the SQLite database (or any other database as required)
DATABASE_URL = "sqlite:///./test.db"  # Update connection string as necessary
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to execute migration
def execute_migration():
    # Create tables
    Base.metadata.create_all(bind=engine)

# Call the migration function to create the Teacher table
if __name__ == "__main__":
    execute_migration()
```