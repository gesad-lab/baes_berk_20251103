```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

# Define the base for ORM models using SQLAlchemy
Base = declarative_base()

# Define the Student model with an email field
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Database setup
DATABASE_URL = "sqlite:///students.db"  # Update with your actual database URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def apply_migrations():
    """Applies database migrations to ensure the schema is up to date."""
    try:
        # Create all tables (will not recreate existing ones)
        Base.metadata.create_all(engine)
        
    except exc.SQLAlchemyError as e:
        # Log the error with detailed context
        print(f"Database migration failed: {str(e)}")
        raise

# Ensures that migrations are applied during application startup
if __name__ == "__main__":
    apply_migrations()
```