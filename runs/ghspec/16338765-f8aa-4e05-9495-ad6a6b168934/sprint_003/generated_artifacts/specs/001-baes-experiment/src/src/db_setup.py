```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for declarative models
Base = declarative_base()

class Course(Base):
    __tablename__ = 'Course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Course name field, required
    level = Column(String, nullable=False)  # Course level field, required

def setup_database():
    # Create the engine and session
    engine = create_engine("sqlite:///./test.db")  # Example connection string
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create all tables in the database (including new Course table)
    Base.metadata.create_all(engine)  # This will now create both tables: Students and Courses
```
