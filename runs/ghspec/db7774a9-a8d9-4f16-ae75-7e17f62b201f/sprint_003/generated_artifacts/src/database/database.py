```python
# src/database/database.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize SQLAlchemy engine
DATABASE_URL = "your_database_url_here"  # Replace with actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

class Course(Base):
    """Course entity representing the courses in the system."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)  # Primary key for Course
    name = Column(String, nullable=False)  # The name of the course
    level = Column(String, nullable=False)  # The level of the course

def init_db():
    """Create all database tables if they don't exist."""
    Base.metadata.create_all(bind=engine)  # Create tables for all models

def upgrade():
    """Perform database migrations. Add the Course table."""
    # Create Course table within migration process
    Course.__table__.create(bind=engine, checkfirst=True)

def downgrade():
    """Rollback database migrations. Drop the Course table."""
    # Drop Course table if it exists
    Course.__table__.drop(bind=engine, checkfirst=True)
```