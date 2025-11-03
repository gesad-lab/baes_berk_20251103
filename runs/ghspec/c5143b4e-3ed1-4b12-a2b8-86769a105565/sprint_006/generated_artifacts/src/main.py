```python
from fastapi import FastAPI, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course, Teacher
from src.schemas import CourseUpdate

app = FastAPI()

@app.put("/courses/{course_id}/assignTeacher")
def assign_teacher_to_course(
    course_id: int = Path(..., title="The ID of the course to assign a teacher"),
    teacher_id: int,
    db: Session = Depends(get_db)
):
    # Validate if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found", "details": {}}})
    
    # Validate if the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Teacher not found", "details": {}}})
    
    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.commit()
    
    return course

@app.delete("/courses/{course_id}/removeTeacher")
def remove_teacher_from_course(
    course_id: int = Path(..., title="The ID of the course to remove the teacher from"),
    db: Session = Depends(get_db)
):
    # Validate if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found", "details": {}}})

    # Remove the teacher from the course
    course.teacher_id = None
    db.commit()
    
    return course
```