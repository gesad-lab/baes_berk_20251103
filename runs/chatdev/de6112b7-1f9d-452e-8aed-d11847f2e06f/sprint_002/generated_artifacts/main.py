'''
Implements the FastAPI application and includes the API router.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from api import router
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
    Base.metadata.create_all(bind=engine)
# Include the API router
app.include_router(router)