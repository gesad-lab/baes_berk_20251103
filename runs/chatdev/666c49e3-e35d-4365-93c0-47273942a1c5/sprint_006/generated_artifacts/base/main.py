'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from routes import router
from database import init_db
app = FastAPI()
# Initialize the database
init_db()
# Include the router for the student, course, and teacher routes
app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)