```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import aiosqlite

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@router.post("/courses", response_model=CourseResponse)
async def create_course(course: CourseCreate):
    """Create a new course in the database."""
    # Validate input and add error handling
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Name and level are required.")       

    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("""
            INSERT INTO courses (name, level) VALUES (?, ?)
        """, (course.name, course.level))
        await db.commit()
        course_id = cursor.lastrowid

    return CourseResponse(id=course_id, name=course.name, level=course.level)

@router.get("/courses", response_model=list[CourseResponse])
async def read_courses():
    """Retrieve the list of all courses."""
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("SELECT id, name, level FROM courses")
        courses = await cursor.fetchall()

    # Create response models from the fetched data
    return [CourseResponse(id=row[0], name=row[1], level=row[2]) for row in courses]
```