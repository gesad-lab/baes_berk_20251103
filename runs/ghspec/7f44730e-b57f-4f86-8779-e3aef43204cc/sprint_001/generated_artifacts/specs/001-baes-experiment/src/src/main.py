from fastapi import FastAPI
from db.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

# Import API routes
import api.student