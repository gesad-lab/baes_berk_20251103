```python
# src/main.py
from fastapi import FastAPI
from db.database import engine
from models.course import Course
from api.course import router as course_router

# Initialize the FastAPI application
app = FastAPI()

# Create the database tables automatically upon startup
@app.on_event("startup")
async def startup_event():
    # Create the course table if it doesn't already exist
    Course.metadata.create_all(engine)

# Include the course router to handle course-related endpoints
app.include_router(course_router)

# Other existing API endpoints can be defined below...
```