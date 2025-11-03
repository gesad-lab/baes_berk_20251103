from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the SQLite database schema automatically on app startup
def create_database():
    """
    Create the SQLite database schema if it does not exist.
    This function is called during app startup to ensure tables are available.
    """
    Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """
    Event handler for application startup.
    Calls the create_database function to ensure that the database schema is created.
    """
    create_database()

# Other API endpoints would go here (Create, Retrieve, Update, Delete)