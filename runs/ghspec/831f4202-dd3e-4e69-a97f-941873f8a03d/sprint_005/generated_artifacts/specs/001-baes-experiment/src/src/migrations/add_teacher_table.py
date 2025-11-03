```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Teacher(Base):
    """Represents a teacher in the educational management system."""

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"

# Database initialization function
DATABASE_URL = "sqlite:///./test.db"  # Update with actual database URL if needed
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(bind=engine)

def create_teacher(db_session, name: str, email: str):
    """Create a new teacher record in the database.

    Args:
        db_session: The database session object to use for creating the record.
        name: The name of the teacher.
        email: The email address of the teacher.
        
    Raises:
        IntegrityError: If email is not unique.
        
    Returns:
        Teacher: The created teacher instance.
    """
    new_teacher = Teacher(name=name, email=email)
    try:
        db_session.add(new_teacher)
        db_session.commit()
        db_session.refresh(new_teacher)
        return new_teacher
    except IntegrityError:
        db_session.rollback()
        raise ValueError("This email is already associated with another teacher.")

# Call init_db during application startup to ensure the Teacher table is created
init_db()
```