```python
# src/main.py

from fastapi import FastAPI
from src.api.student_routes import router as student_router
from src.api.course_routes import router as course_router
from src.api.teacher_routes import router as teacher_router

app = FastAPI()

# Include existing routes for students and courses
app.include_router(student_router)
app.include_router(course_router)

# Include new routes for teachers
app.include_router(teacher_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Educational Institution API!"}
```