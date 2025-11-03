```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Define the base class for declarative models
Base = declarative_base()

# Create the Teacher model
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# Database connection URL (replace with your own configuration)
DATABASE_URL = "sqlite:///./test.db"

# Create an engine and a configured "Session" class
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Initialize the database when the module is run
if __name__ == "__main__":
    init_db()
```