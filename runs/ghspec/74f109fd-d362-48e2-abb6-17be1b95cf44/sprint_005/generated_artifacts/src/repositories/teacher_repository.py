```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Teacher(Base):
    """Represents a Teacher entity in the database."""
    
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    name = Column(String(255), nullable=False)  # Teacher's name, max length of 255 characters
    email = Column(String, nullable=False)  # Teacher's email address, must be unique and valid

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"

# Database engine initialization (replace 'sqlite:///example.db' with actual database URL)
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
def create_tables():
    """Create all tables in the database, including the Teacher table."""
    Base.metadata.create_all(engine)

# Invoke this function to create tables if needed
create_tables()
```