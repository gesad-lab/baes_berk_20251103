```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import aiosqlite

app = FastAPI()

class CourseCreate(BaseModel):
    name: str = Field(..., example="Introduction to Programming")
    level: str = Field(..., example="Beginner")

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@app.post("/courses", response_model=CourseResponse)
async def create_course(course: CourseCreate):
    """Create a new course in the database."""
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Both 'name' and 'level' are required fields."
                }
            }
        )

    try:
        async with aiosqlite.connect("database.db") as db:
            await db.execute("INSERT INTO courses (name, level) VALUES (?, ?)", (course.name, course.level))
            await db.commit()
            # Fetching the id of the newly created course
            cursor = await db.execute("SELECT id FROM courses WHERE name = ? AND level = ?", (course.name, course.level))
            course_id = await cursor.fetchone()
            return CourseResponse(id=course_id[0], name=course.name, level=course.level)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": "E002",
                    "message": "An error occurred while creating the course.",
                    "details": str(e)  # Log error for debugging, but do not expose it in a production environment
                }
            }
        )

@app.get("/courses", response_model=list[CourseResponse])
async def get_courses():
    """Retrieve a list of all courses."""
    try:
        async with aiosqlite.connect("database.db") as db:
            cursor = await db.execute("SELECT id, name, level FROM courses")
            courses = await cursor.fetchall()
            return [CourseResponse(id=row[0], name=row[1], level=row[2]) for row in courses]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": {
                    "code": "E003",
                    "message": "An error occurred while fetching the courses.",
                    "details": str(e)
                }
            }
        )

async def migrate():
    """Perform database migration to add the courses table."""
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                level TEXT NOT NULL
            )
        """)
        await db.commit()
```