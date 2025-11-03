'''
Implements the FastAPI application and initializes the database.
'''
from fastapi import FastAPI
from database import init_db
from api import router
app = FastAPI()
@app.on_event("startup")
def startup_event():
    init_db()
app.include_router(router)