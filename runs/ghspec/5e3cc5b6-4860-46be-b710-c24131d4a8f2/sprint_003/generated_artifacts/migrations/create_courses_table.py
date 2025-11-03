```python
from fastapi import FastAPI
from src.routes.course_routes import router as course_router

app = FastAPI()

# Include the course routes in the FastAPI application
app.include_router(course_router, prefix="/courses", tags=["courses"])

# Existing routes and functionality
```