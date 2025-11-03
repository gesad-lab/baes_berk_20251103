'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from routes import router
from database import init_db
app = FastAPI()
@app.on_event("startup")
def startup_event():
    init_db()
app.include_router(router)