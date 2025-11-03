```python
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Update with your actual database URL
Base = declarative_base()

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, nullable=False)
    level = sa.Column(sa.String, nullable=False)

# Create an engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create the database tables
def init_db():
    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(bind=engine)

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Call to initialize the database (create tables)
if __name__ == "__main__":
    init_db()
```