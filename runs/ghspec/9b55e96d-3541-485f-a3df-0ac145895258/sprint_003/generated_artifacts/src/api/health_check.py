```python
# src/main.py

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from src.api.health_check import check_courses_table

DATABASE_URL = "sqlite:///./test.db"  # Define your database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Define the Course model
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Initialize the database and the courses table
@app.on_event("startup")
def startup():
    try:
        # Check if the courses table exists and create it if not
        Base.metadata.create_all(bind=engine)
        check_courses_table()  # Custom function to ensure the courses table is initialized
    except SQLAlchemyError as e:
        # Log error and raise an HTTP exception
        print(f"Database error during startup: {str(e)}")
        raise HTTPException(status_code=500, detail="Database initialization error.")

# Sample health check endpoint
@app.get("/")
def read_root():
    return {"msg": "Welcome to the Course Management API!"}

# The rest of your FastAPI application code here...
```