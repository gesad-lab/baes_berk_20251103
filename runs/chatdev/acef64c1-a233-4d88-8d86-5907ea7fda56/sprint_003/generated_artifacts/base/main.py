'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import create_database
from routes import router
def create_app() -> FastAPI:
    app = FastAPI()
    create_database()
    app.include_router(router)
    return app
app = create_app()