from fastapi import FastAPI
from src.routes.teachers import router as teacher_router

app = FastAPI()

# Include the teacher router into the main application
app.include_router(teacher_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the educational application!"}