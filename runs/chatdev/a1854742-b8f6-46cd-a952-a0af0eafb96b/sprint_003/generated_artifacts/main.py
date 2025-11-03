'''
Runs the FastAPI application using Uvicorn.
'''
import uvicorn
from fastapi import FastAPI
from database import engine, Base
from routers import router
# Create the FastAPI app
app = FastAPI()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Include the router for student and course routes
app.include_router(router)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)