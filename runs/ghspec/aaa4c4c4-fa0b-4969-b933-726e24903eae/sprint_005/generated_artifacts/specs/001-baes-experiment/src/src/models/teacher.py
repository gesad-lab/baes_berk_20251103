```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Teacher(Base):
    """Model representing a teacher in the educational system."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"

# Setup database engine and session (simulating existing setup from previous context)
DATABASE_URL = "sqlite:///./test.db"  # Example SQLite URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the Teacher table in the database if it does not exist
def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(bind=engine)
    
# Call init_db to ensure the Teacher table is created
init_db()
```