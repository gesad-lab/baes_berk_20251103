'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from alembic import command
from alembic.config import Config
from routers import router  # Import the combined router from routers
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)  # Include the combined router
    return app
app = create_app()
if __name__ == "__main__":
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Run migrations before starting the app
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)