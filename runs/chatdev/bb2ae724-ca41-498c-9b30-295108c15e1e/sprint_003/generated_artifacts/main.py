'''
Entry point of the application.
'''
from fastapi import FastAPI
from database import init_db
from routes import student_router
app = FastAPI()
@app.on_event("startup")
async def startup_event():
    init_db()
app.include_router(student_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)