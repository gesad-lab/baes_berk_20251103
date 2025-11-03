'''
Migration script to add Course table to the database.
'''
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import inspect
Base = declarative_base()
DATABASE_URL = "sqlite:///./students.db"
class Course(Base):  # New Course model for migration
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
def upgrade():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    inspector = inspect(engine)
    # Create the courses table if it doesn't exist
    if 'courses' not in inspector.get_table_names():
        Base.metadata.create_all(engine)  # Create the table if it doesn't exist
if __name__ == "__main__":
    upgrade()