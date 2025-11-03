'''
Handles the database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def init_db():
    '''
    Create all tables in the database.
    '''
    Base.metadata.create_all(bind=engine)  # This will now include the Course and Teacher tables
# Call to initialize the database
init_db()  