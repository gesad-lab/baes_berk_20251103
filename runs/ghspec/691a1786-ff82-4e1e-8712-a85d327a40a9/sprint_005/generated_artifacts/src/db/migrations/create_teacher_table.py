```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for our models
Base = declarative_base()

class Teacher(Base):
    """Model for the Teacher table."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

def create_teacher_table():
    """Create the Teacher table in the database."""
    # Database URL for the migration (replace with your actual database)
    DATABASE_URL = 'sqlite:///./test.db'
    engine = create_engine(DATABASE_URL)

    # Create the Teacher table only if it does not already exist
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_teacher_table()
```