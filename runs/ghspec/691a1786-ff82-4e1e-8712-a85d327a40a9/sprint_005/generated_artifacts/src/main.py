```python
# File: src/main.py

from fastapi import FastAPI
from src.routes.student_routes import router as student_router
from src.routes.teacher_routes import router as teacher_router

app = FastAPI()

# Include student routes
app.include_router(student_router, prefix="/students", tags=["students"])

# Include teacher routes
app.include_router(teacher_router, prefix="/teachers", tags=["teachers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the school management API"}

# Add error handling globally if necessary
@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "details": str(exc)},
    )
```