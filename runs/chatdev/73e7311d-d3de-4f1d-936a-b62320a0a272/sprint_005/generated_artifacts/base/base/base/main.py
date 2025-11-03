'''
Main application entry point.
'''
import uvicorn
from fastapi import FastAPI
from database import init_db
app = FastAPI()
# Initialize the database
init_db()
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)