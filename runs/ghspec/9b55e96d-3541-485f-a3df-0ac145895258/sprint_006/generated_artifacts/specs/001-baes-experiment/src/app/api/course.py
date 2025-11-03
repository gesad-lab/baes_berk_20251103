from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher
from database import get_db

router = APIRouter()

@router.post("/courses/{course_id}/assign-teacher")
async def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """Assign a teacher to a specific course.

    Parameters:
    - course_id: ID of the course to which the teacher is being assigned.
    - teacher_id: ID of the teacher being assigned to the course.
    
    Returns:
    - Confirmation message upon successful assignment or error details if the operation fails.
    """
    # Retrieve the course from the database, raise 404 if not found
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found."}})
    
    # Check if the course already has an assigned teacher
    if course.teacher_id is not None:
        raise HTTPException(status_code=409, detail={"error": {"code": "E002", "message": "Course already has a teacher assigned."}})

    # Retrieve the teacher from the database, raise 404 if not found
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Teacher not found."}})
    
    # Assign the teacher to the course and commit the changes
    course.teacher_id = teacher_id
    db.commit()
    return {"message": "Teacher assigned successfully"}

@router.get("/courses/{course_id}", response_model=dict)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """Retrieve details of a specific course along with its assigned teacher.

    Parameters:
    - course_id: ID of the course to retrieve.
    
    Returns:
    - Course details with teacher information or error details if the operation fails.
    """
    # Retrieve the course from the database, raise 404 if not found
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found."}})
    
    # Prepare the response structure including teacher information if available
    return {
        "id": course.id,
        "title": course.title,
        "teacher": {
            "id": course.teacher.id,
            "name": course.teacher.name,
            "email": course.teacher.email,
        } if course.teacher else None
    }