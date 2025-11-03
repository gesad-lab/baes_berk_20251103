```python
# src/database.py
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Database connection setup
DATABASE_URL = "sqlite:///app.db"  # Update as per your environment
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Teacher(Base):
    """Model representing the Teacher entity."""
    __tablename__ = 'teachers'
    
    teacher_id = Column(Integer, Sequence('teacher_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

def create_database():
    """Create the database and tables."""
    Base.metadata.create_all(engine)

def migrate_database():
    """Perform migrations for the application setup."""
    # Here you can include migration logic, e.g., adding new tables 
    # while ensuring the existing ones remain unaffected.
    create_database()

if __name__ == "__main__":
    migrate_database()
```