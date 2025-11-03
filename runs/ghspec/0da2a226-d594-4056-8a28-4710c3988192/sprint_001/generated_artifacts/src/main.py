```python
import logging
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

# Initialize FastAPI application
app = FastAPI()

# Configure logging
logging.basicConfig(
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
    level=logging.INFO
)

# Create database engine
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables on startup
@app.on_event("startup")
async def startup_event():
    logging.info("Starting up the application...")
    Base.metadata.create_all(bind=engine)
    logging.info("Database tables created.")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Sample endpoint to demonstrate logging
@app.get("/")
async def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Welcome to the Student Entity API!"}
```