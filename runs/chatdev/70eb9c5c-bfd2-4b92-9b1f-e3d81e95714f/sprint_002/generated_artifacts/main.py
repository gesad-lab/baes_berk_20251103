'''
Database migration script to add email field to Student entity.
'''
from sqlalchemy import create_engine, Column, String, Integer  # Added Integer import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
def migrate():
    Base.metadata.create_all(bind=engine)
if __name__ == "__main__":
    migrate()