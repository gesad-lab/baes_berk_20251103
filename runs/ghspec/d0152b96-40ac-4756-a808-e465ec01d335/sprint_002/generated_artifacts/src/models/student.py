```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    """Model for the Student entity."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name field is required
    email = Column(String, nullable=False)  # Email field is required and of type String

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

# Ensure the database schema is created/updated when the application starts
engine = create_engine("sqlite:///./students.db")
Base.metadata.create_all(engine)
```