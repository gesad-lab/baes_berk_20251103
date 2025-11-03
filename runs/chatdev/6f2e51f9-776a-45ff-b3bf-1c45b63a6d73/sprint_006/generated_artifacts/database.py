'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base  # Import Base to create tables
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create the database tables if they don't exist
def init_db():
    Base.metadata.create_all(bind=engine)