'''
Handles the SQLite database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Database:
    def create_database(self):
        Base.metadata.create_all(bind=engine)
        # Ensure Course table is created
        if not engine.dialect.has_table(engine, 'courses'):
            Base.metadata.tables['courses'].create(bind=engine)