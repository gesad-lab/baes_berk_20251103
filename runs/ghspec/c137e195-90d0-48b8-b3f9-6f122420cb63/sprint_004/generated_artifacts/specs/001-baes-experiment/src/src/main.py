```python
from fastapi import FastAPI
from database.db import init_db
from api.student_courses import router as student_courses_router

app = FastAPI()

@app.on_event("startup")
def startup():
    """Initialize the database on application startup."""
    init_db()

# Include new router for student-course associations
app.include_router(student_courses_router)
```