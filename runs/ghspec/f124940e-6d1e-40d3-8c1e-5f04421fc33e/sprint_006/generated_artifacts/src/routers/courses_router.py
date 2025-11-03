from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Course, Teacher
from .database import get_db  # Assuming get_db provides the database session

router = APIRouter()

@router.post("/courses/{course_id}/assign_teacher", response_model=Course)
def assign_teacher(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=400, detail="Invalid teacher_id provided")

    course.teacher_id = teacher_id
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@router.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.delete("/courses/{course_id}/unassign_teacher", response_model=Course)
def unassign_teacher(course_id: int, db: Session = Depends(get_db)):
    """
    Unassign a teacher from the specified course.

    Args:
        course_id (int): The ID of the course to unassign the teacher from.
        db (Session): Database session dependency.

    Returns:
        Course: The updated course details with teacher unassigned (i.e., teacher set to None).
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Unassign the teacher by setting the teacher_id to None
    course.teacher_id = None
    db.add(course)
    db.commit()
    db.refresh(course)
    return course