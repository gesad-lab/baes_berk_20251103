'''
Runs the FastAPI application.
'''
from fastapi import FastAPI
from api import router
from database import create_database
app = FastAPI()
# Create the database and tables
create_database()
# Include the router
app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)