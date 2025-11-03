from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL and create the database engine
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)

# Initialize SQLAlchemy base and create all tables
Base = declarative_base()
Base.metadata.create_all(engine)

# Create a FastAPI application instance
app = FastAPI()

@app.get("/health")
def read_health():
    """Check the health status of the API."""
    return {"status": "healthy"}

# Entry point to start the application
if __name__ == "__main__":
    import uvicorn
    # Running the app with uvicorn server
    uvicorn.run(app, host="127.0.0.1", port=8000)