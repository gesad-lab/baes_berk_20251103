'''
Main entry point of the application.
'''
from fastapi import FastAPI
from database import init_db
from api import router as api_router
import uvicorn
from alembic import command
from alembic.config import Config
def run_migrations():
    alembic_cfg = Config("alembic.ini")  # Ensure you have an alembic.ini file configured
    command.upgrade(alembic_cfg, "head")
def create_app() -> FastAPI:
    app = FastAPI()
    run_migrations()  # Run migrations here before initializing the database
    init_db()  # Initialize the database after migrations
    app.include_router(api_router)
    return app
if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8000)