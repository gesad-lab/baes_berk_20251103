from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI application
app = FastAPI()

# Read SQLite database path from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Management API"}

# Further application configurations can be done here, including routing the endpoints
# to the student-related functionalities when they are implemented.

if __name__ == "__main__":
    import uvicorn
    # Start the FastAPI application with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)