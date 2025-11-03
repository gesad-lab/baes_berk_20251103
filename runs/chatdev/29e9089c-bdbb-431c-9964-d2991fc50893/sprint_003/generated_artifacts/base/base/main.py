'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import init_db
from routers import student
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(student.router)
    return app
app = create_app()
@app.on_event("startup")
async def startup_event():
    init_db()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)