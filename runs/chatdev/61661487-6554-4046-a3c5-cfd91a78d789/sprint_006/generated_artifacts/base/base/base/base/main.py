'''
Database migration script to add email column to Student table.
'''
from sqlalchemy import Column, Integer, String  # Ensure Integer is imported
from sqlalchemy.orm import sessionmaker, declarative_base  # Update import for declarative_base
from sqlalchemy import create_engine
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email column
def migrate():
    Base.metadata.create_all(bind=engine)  # This will create the new column if it doesn't exist
if __name__ == "__main__":
    migrate()