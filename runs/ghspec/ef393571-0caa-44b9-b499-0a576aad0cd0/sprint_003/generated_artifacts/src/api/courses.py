```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import aiosqlite

app = FastAPI()

# Pydantic models for request and response
class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

# Database migration function
async def migrate():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                level TEXT NOT NULL
            )
        """)
        await db.commit()

@app.on_event("startup")
async def startup_event():
    await migrate()

# List to hold courses in memory (replace with actual database calls in production)
courses_db = []

@app.post("/courses", response_model=CourseResponse)
async def create_course(course: CourseCreate):
    # Validate the incoming course data
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both 'name' and 'level' are required.")
    
    # Simulate adding the course to the database
    new_course_id = len(courses_db) + 1  # Incremental ID for simulation
    new_course = {"id": new_course_id, "name": course.name, "level": course.level}
    courses_db.append(new_course)
    
    return new_course

@app.get("/courses", response_model=List[CourseResponse])
async def get_courses():
    return courses_db
```