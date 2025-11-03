```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine for the SQLite database, using a local file
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)

# Base class for the declarative model
Base = declarative_base()

# Session local for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```