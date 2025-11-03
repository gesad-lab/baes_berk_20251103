```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData

# Define the Base for declarative class definitions
Base = declarative_base()

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"

# Database connection parameters (to be modified as necessary)
DATABASE_URL = "sqlite:///./test.db"  # Use your actual database URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Function to initialize the database tables
def init_db():
    Base.metadata.create_all(bind=engine)

# A helper function to get database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Run database initialization (consider placing this logic in a more appropriate location)
if __name__ == "__main__":
    init_db()
```