from sqlalchemy import Column, Integer, String
from db.database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Function to ensure the database schema is created automatically
def create_database_schema(engine):
    """Create the database schema automatically upon application startup."""
    Base.metadata.create_all(engine)  # Create all tables in the engine's database

# Note: This function should be called in the main application file during startup,
# passing the database engine to it so that the tables can be created if they do not exist.