```python
# src/db/migrations/xxxx_add_teacher_table.py

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for declarative model
Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

def upgrade(engine_url: str):
    # Create a new SQLAlchemy engine instance
    engine = create_engine(engine_url)
    
    # Create all tables
    Base.metadata.create_all(engine)

def downgrade(engine_url: str):
    # Dropping the teacher table if it exists
    engine = create_engine(engine_url)
    conn = engine.connect()
    conn.execute("DROP TABLE IF EXISTS teachers")
    conn.close()

# This function can be used to run the upgrade or downgrade scripts.
def run_migration(command: str, engine_url: str):
    if command == 'upgrade':
        upgrade(engine_url)
    elif command == 'downgrade':
        downgrade(engine_url)
    else:
        print("Invalid command. Use 'upgrade' or 'downgrade'.")
```
