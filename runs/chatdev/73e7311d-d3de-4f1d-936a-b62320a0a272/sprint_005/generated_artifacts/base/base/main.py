'''
Main application entry point.
'''
import uvicorn
from fastapi import FastAPI, HTTPException
from database import init_db, get_db
from models import Course
from schemas import CourseCreate, CourseResponse
app = FastAPI()
# Initialize the database
init_db()
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate):
    db = next(get_db())
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/{course_id}", response_model=CourseResponse)
def read_course(course_id: int):
    db = next(get_db())
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)