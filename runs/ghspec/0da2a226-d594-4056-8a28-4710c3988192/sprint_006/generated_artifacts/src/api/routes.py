from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher
from database import get_db

router = APIRouter()

@router.post("/assign_teacher/{course_id}/{teacher_id}", response_model=Course)
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Assign a Teacher to a Course.

    Args:
        course_id (int): The ID of the Course to assign the Teacher to.
        teacher_id (int): The ID of the Teacher to be assigned.
        db (Session): The database session.

    Returns:
        Course: The updated Course with Teacher information.
    
    Raises:
        HTTPException: If the Course or Teacher does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    return course

@router.get("/courses", response_model=list[Course])
def retrieve_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of Courses with their assigned Teachers.

    Args:
        db (Session): The database session.

    Returns:
        list[Course]: A list of Courses including Teacher details.
    """
    courses = db.query(Course).all()
    return courses

# Register the router in the main application
def include_router(app):
    app.include_router(router)