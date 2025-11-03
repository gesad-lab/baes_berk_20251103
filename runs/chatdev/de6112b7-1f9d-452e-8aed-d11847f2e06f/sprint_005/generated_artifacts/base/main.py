'''
Implements the FastAPI application and includes the API router.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from api import router
from alembic import command
from alembic.config import Config
# Create the FastAPI app
app = FastAPI()
# Allow CORS for all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create the database schema on startup
@app.on_event("startup")
def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
# Include the API router
app.include_router(router)