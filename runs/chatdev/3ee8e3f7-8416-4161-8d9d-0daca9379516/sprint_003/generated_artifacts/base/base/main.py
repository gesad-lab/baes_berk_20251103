'''
Main entry point for the Student application.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router
from database import engine, Base
# Create the FastAPI app
app = FastAPI()
# Allow CORS for the GUI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create the database schema on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Include the router for student-related operations
app.include_router(router)