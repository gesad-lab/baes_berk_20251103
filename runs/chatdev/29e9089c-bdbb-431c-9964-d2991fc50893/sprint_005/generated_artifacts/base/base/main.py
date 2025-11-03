'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import init_db
from routers import student, course  # Added course import to include course routes
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(student.router)
    app.include_router(course.router)  # Included course router to enable course routes
    return app
app = create_app()
@app.on_event("startup")
async def startup_event():
    init_db()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)