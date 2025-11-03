```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database URL for SQLite database
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)

def init_db():
    """
    Initializes the database by creating the necessary tables.

    This function binds the engine to the Base metadata and creates all 
    tables defined in the models. It should be called at the application 
    startup.
    """
    Base.metadata.create_all(bind=engine)
```