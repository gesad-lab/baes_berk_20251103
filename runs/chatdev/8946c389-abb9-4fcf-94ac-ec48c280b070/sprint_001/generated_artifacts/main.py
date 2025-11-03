'''
Main entry point for the FastAPI application and GUI.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from api import router as api_router
import gui
def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    app.include_router(api_router)
    return app
if __name__ == "__main__":
    init_db()  # Initialize the database schema
    app = create_app()
    gui.run_gui()  # Start the GUI