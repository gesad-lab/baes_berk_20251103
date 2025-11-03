'''
Database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import inspect  # Import inspect for checking table existence
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db() -> Session:
    '''
    Create a new database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create the database tables only if they do not exist
if not inspect(engine).has_table("students"):
    Base.metadata.create_all(bind=engine)
if not inspect(engine).has_table("courses"):
    Base.metadata.create_all(bind=engine)
if not inspect(engine).has_table("student_courses"):
    Base.metadata.create_all(bind=engine)