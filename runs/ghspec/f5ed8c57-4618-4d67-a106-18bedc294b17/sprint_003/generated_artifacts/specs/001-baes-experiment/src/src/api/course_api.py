```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import logging

# Set up structured logging
logging.basicConfig(level=logging.INFO, format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
logger = logging.getLogger(__name__)

app = FastAPI()

# Mock DB for illustration purposes - replace with actual database access logic
courses_db = {}

class Course(BaseModel):
    name: str
    level: str

@app.post("/courses", response_model=Course, status_code=201)
def create_course(course: Course):
    # Generate a unique ID for the course (mocking a DB auto-increment ID for demo)
    course_id = len(courses_db) + 1
    courses_db[course_id] = course
    logger.info(f"Course created: {course_id}, {course.dict()}")
    return {**course.dict(), "id": course_id}

@app.get("/courses/{course_id}", response_model=Course)
def retrieve_course(course_id: int):
    if course_id not in courses_db:
        logger.error(f"Course not found: {course_id}")
        raise HTTPException(status_code=404, detail="Course not found")
    logger.info(f"Course retrieved: {course_id}, {courses_db[course_id].dict()}")
    return {**courses_db[course_id].dict(), "id": course_id}

@app.get("/courses", response_model=List[Course])
def list_courses():
    logger.info("Listing all courses")
    return [{"id": course_id, **course.dict()} for course_id, course in courses_db.items()]
```