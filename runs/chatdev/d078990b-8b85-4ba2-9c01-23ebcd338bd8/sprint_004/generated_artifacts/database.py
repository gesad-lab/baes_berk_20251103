'''
Database connection and initialization.
'''
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from models import Base
from alembic import command
from alembic.config import Config as AlembicConfig
import os
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    '''
    Dependency to get the database session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def init_db():
    '''
    Initialize the database and create tables.
    '''
    # Check if the database exists and apply migrations
    if os.path.exists("students.db"):
        alembic_cfg = AlembicConfig("alembic.ini")
        command.upgrade(alembic_cfg, "head")
    else:
        Base.metadata.create_all(bind=engine)