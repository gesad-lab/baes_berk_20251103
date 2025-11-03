```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for declarative models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"

# Database initialization function
def init_db(database_url: str):
    """
    Initializes the database and creates the necessary tables, including indexing for performance.

    :param database_url: The database connection URL
    """
    # Create a new database engine
    engine = create_engine(database_url)

    # Create all tables in the engine (i.e., create the students table)
    Base.metadata.create_all(engine)

    # Create an indexed field for the name column to speed up retrieval
    with engine.connect() as connection:
        connection.execute("CREATE INDEX IF NOT EXISTS idx_students_name ON students (name);")

# Session factory for database interaction
Session = sessionmaker(bind=create_engine('sqlite:///students.db'))

# Initialize the database on startup
if __name__ == "__main__":
    init_db('sqlite:///students.db')
```